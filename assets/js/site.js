// Recursos do site no GitHub Pages. Tudo aqui é melhoria: sem JavaScript, as páginas continuam legíveis.
// - menu lateral no celular e tema claro/escuro;
// - links para arquivos de trabalho (fora do site) passam a abrir no GitHub;
// - diagramas Mermaid desenhados no navegador;
// - busca nas páginas (busca.json);
// - progresso marcado e guardado no navegador (progresso.md);
// - questões respondidas com um clique (simulados/questoes/dominio-N.md);
// - flashcards em modo cartão (flashcards/*.md).
(function () {
  "use strict";

  var BASE = document.body.getAttribute("data-base") || "/";
  var REPO = document.body.getAttribute("data-repo") || "";
  var MERMAID = "https://cdn.jsdelivr.net/npm/mermaid@12.1.0/dist/mermaid.min.js";
  // Pastas e arquivos que o _config.yml deixa fora do site.
  var FORA_DO_SITE = ["CLAUDE.md", "pendencias/", "scripts/", "fontes/", "templates/"];
  var caminho = location.pathname.slice(BASE.length - 1);

  function guardar(chave, valor) {
    try { localStorage.setItem(chave, JSON.stringify(valor)); } catch (e) { /* navegador sem armazenamento */ }
  }
  function ler(chave, padrao) {
    try { var v = localStorage.getItem(chave); return v ? JSON.parse(v) : padrao; } catch (e) { return padrao; }
  }
  function criar(tag, classe, texto) {
    var el = document.createElement(tag);
    if (classe) el.className = classe;
    if (texto != null) el.textContent = texto;
    return el;
  }
  function semAcento(texto) {
    return texto.normalize("NFD").replace(/[̀-ͯ]/g, "").toLowerCase();
  }

  // ---------- Menu no celular ----------
  var botaoMenu = document.querySelector(".botao-menu");
  function abrirMenu(abrir) {
    document.body.classList.toggle("menu-aberto", abrir);
    botaoMenu.setAttribute("aria-expanded", String(abrir));
  }
  botaoMenu.addEventListener("click", function () { abrirMenu(!document.body.classList.contains("menu-aberto")); });
  document.addEventListener("keydown", function (e) { if (e.key === "Escape") abrirMenu(false); });
  document.getElementById("conteudo").addEventListener("click", function () { abrirMenu(false); });
  var atual = document.querySelector('.menu a[aria-current="page"]');
  if (atual) atual.scrollIntoView({ block: "center" });

  // ---------- Tema claro/escuro ----------
  function temaEscuro() {
    var t = document.documentElement.getAttribute("data-theme");
    return t ? t === "dark" : window.matchMedia("(prefers-color-scheme: dark)").matches;
  }
  document.querySelector(".botao-tema").addEventListener("click", function () {
    var novo = temaEscuro() ? "light" : "dark";
    document.documentElement.setAttribute("data-theme", novo);
    try { localStorage.setItem("tema", novo); } catch (e) { /* sem armazenamento */ }
    desenharDiagramas();
  });
  // ---------- Links para arquivos fora do site ----------
  Array.prototype.forEach.call(document.querySelectorAll("#conteudo a[href]"), function (a) {
    var url = new URL(a.getAttribute("href"), location.href);
    if (url.origin !== location.origin || url.pathname.indexOf(BASE) !== 0) return;
    var resto = decodeURIComponent(url.pathname.slice(BASE.length));
    var fora = FORA_DO_SITE.some(function (p) { return resto === p || resto.indexOf(p) === 0; });
    if (fora) a.href = REPO + (resto.slice(-1) === "/" ? "/tree/main/" : "/blob/main/") + resto + url.hash;
  });

  // ---------- Diagramas Mermaid ----------
  var diagramas = Array.prototype.map.call(
    document.querySelectorAll("div.language-mermaid, pre > code.language-mermaid"),
    function (bloco) {
      var alvo = bloco.tagName === "CODE" ? bloco.parentNode : bloco;
      var div = criar("div", "diagrama");
      div.setAttribute("data-fonte", alvo.textContent);
      alvo.parentNode.replaceChild(div, alvo);
      return div;
    });
  var mermaidPronto = null;
  function carregarMermaid() {
    if (!mermaidPronto) {
      mermaidPronto = new Promise(function (ok, falha) {
        var s = document.createElement("script");
        s.src = MERMAID;
        s.onload = function () { ok(window.mermaid); };
        s.onerror = falha;
        document.head.appendChild(s);
      });
    }
    return mermaidPronto;
  }
  function desenharDiagramas() {
    if (!diagramas.length) return;
    carregarMermaid().then(function (mermaid) {
      mermaid.initialize({ startOnLoad: false, theme: temaEscuro() ? "dark" : "default", securityLevel: "strict" });
      diagramas.forEach(function (div) {
        div.removeAttribute("data-processed");
        div.classList.add("mermaid");
        div.textContent = div.getAttribute("data-fonte");
      });
      return mermaid.run({ nodes: diagramas });
    }).catch(function () {
      // Sem acesso ao Mermaid: mostra o texto do diagrama, como antes.
      diagramas.forEach(function (div) {
        var pre = criar("pre"); pre.appendChild(criar("code", null, div.getAttribute("data-fonte")));
        div.textContent = ""; div.appendChild(pre);
      });
    });
  }
  desenharDiagramas();

  // ---------- Busca ----------
  var campo = document.getElementById("busca");
  var lista = document.getElementById("busca-resultados");
  var indice = null;
  function carregarIndice() {
    if (!indice) {
      indice = fetch(BASE + "busca.json").then(function (r) { return r.json(); }).then(function (paginas) {
        return paginas.map(function (p) { return { t: p.t, u: p.u, x: p.x, tn: semAcento(p.t), xn: semAcento(p.x) }; });
      });
    }
    return indice;
  }
  function trecho(p, termo) {
    var i = p.xn.indexOf(termo);
    if (i < 0) return p.x.slice(0, 140) + "…";
    var ini = Math.max(0, i - 60);
    return (ini > 0 ? "…" : "") + p.x.slice(ini, i + 100) + "…";
  }
  function buscar() {
    var consulta = semAcento(campo.value.trim());
    if (consulta.length < 2) { lista.hidden = true; return; }
    var termos = consulta.split(/\s+/);
    carregarIndice().then(function (paginas) {
      var achados = [];
      paginas.forEach(function (p) {
        var pontos = 0;
        for (var i = 0; i < termos.length; i++) {
          var noTitulo = p.tn.indexOf(termos[i]) >= 0;
          var noTexto = p.xn.indexOf(termos[i]) >= 0;
          if (!noTitulo && !noTexto) return;
          pontos += (noTitulo ? 10 : 0) + (noTexto ? 1 + Math.min(p.xn.split(termos[i]).length - 1, 9) / 10 : 0);
        }
        achados.push({ p: p, pontos: pontos });
      });
      achados.sort(function (a, b) { return b.pontos - a.pontos; });
      lista.textContent = "";
      if (!achados.length) lista.appendChild(criar("li", "busca-vazia", "Nada encontrado para “" + campo.value.trim() + "”."));
      achados.slice(0, 12).forEach(function (a) {
        var li = criar("li"), link = criar("a");
        link.href = a.p.u;
        link.appendChild(criar("strong", null, a.p.t));
        link.appendChild(criar("small", null, trecho(a.p, termos[0])));
        li.appendChild(link);
        lista.appendChild(li);
      });
      lista.hidden = false;
    });
  }
  campo.addEventListener("focus", carregarIndice);
  campo.addEventListener("input", buscar);
  campo.addEventListener("keydown", function (e) {
    var itens = lista.querySelectorAll("a");
    var ativo = lista.querySelector(".ativo");
    var pos = Array.prototype.indexOf.call(itens, ativo ? ativo.firstChild : null);
    if (e.key === "ArrowDown" || e.key === "ArrowUp") {
      e.preventDefault();
      if (!itens.length) return;
      if (ativo) ativo.classList.remove("ativo");
      pos = e.key === "ArrowDown" ? Math.min(pos + 1, itens.length - 1) : Math.max(pos - 1, 0);
      itens[pos].parentNode.classList.add("ativo");
      itens[pos].scrollIntoView({ block: "nearest" });
    } else if (e.key === "Enter" && itens.length) {
      location.href = (ativo ? ativo.firstChild : itens[0]).href;
    } else if (e.key === "Escape") {
      lista.hidden = true;
    }
  });
  document.addEventListener("click", function (e) { if (!e.target.closest(".busca")) lista.hidden = true; });
  document.addEventListener("keydown", function (e) {
    if (e.key === "/" && !/INPUT|TEXTAREA/.test(document.activeElement.tagName)) { e.preventDefault(); campo.focus(); }
  });

  // ---------- Progresso ----------
  var concluidas = ler("progresso", {});
  function chaveDoItem(li) {
    var a = li.querySelector("a[href]");
    return a ? new URL(a.href).pathname : li.textContent.trim();
  }
  function marcarMenu() {
    Array.prototype.forEach.call(document.querySelectorAll(".menu a"), function (a) {
      a.classList.toggle("concluida", !!concluidas[new URL(a.href).pathname]);
    });
  }
  marcarMenu();
  if (/\/progresso\.html$/.test(caminho)) {
    var itens = document.querySelectorAll("#conteudo .task-list-item");
    var barra = criar("div", "ferramentas");
    var contagem = criar("span");
    var medidor = criar("div", "barra"), preenchido = criar("span");
    var zerar = criar("button", null, "Desmarcar tudo");
    zerar.type = "button";
    medidor.appendChild(preenchido);
    barra.appendChild(contagem); barra.appendChild(medidor); barra.appendChild(zerar);
    barra.appendChild(criar("small", "aviso-questao", "As marcações ficam guardadas só neste navegador."));
    var titulo = document.querySelector("#conteudo h1");
    titulo.parentNode.insertBefore(barra, titulo.nextSibling);
    function atualizar() {
      var feitas = 0;
      Array.prototype.forEach.call(itens, function (li) { if (li.querySelector("input").checked) feitas++; });
      contagem.textContent = feitas + " de " + itens.length + " concluídos";
      preenchido.style.width = (itens.length ? 100 * feitas / itens.length : 0) + "%";
      marcarMenu();
    }
    Array.prototype.forEach.call(itens, function (li) {
      var caixa = li.querySelector("input[type=checkbox]");
      var chave = chaveDoItem(li);
      caixa.disabled = false;
      caixa.checked = !!concluidas[chave];
      caixa.setAttribute("aria-label", "Concluído: " + li.textContent.trim());
      caixa.addEventListener("change", function () {
        if (caixa.checked) concluidas[chave] = true; else delete concluidas[chave];
        guardar("progresso", concluidas);
        atualizar();
      });
    });
    zerar.addEventListener("click", function () {
      if (!confirm("Desmarcar todos os itens do progresso?")) return;
      concluidas = {};
      guardar("progresso", concluidas);
      Array.prototype.forEach.call(itens, function (li) { li.querySelector("input").checked = false; });
      atualizar();
    });
    atualizar();
  }

  // ---------- Questões ----------
  if (/\/simulados\/questoes\/dominio-\d+\.html$/.test(caminho)) {
    var questoes = [];
    Array.prototype.forEach.call(document.querySelectorAll("#conteudo h3"), function (h3) {
      if (!/^Questão/.test(h3.textContent.trim())) return;
      var alternativas = null, resposta = null;
      for (var el = h3.nextElementSibling; el && el.tagName !== "H3" && el.tagName !== "HR"; el = el.nextElementSibling) {
        if (!alternativas && el.tagName === "UL") alternativas = el;
        if (!resposta && el.tagName === "DETAILS") resposta = el;
      }
      if (!alternativas || !resposta) return;
      var m = resposta.textContent.match(/Resposta:\s*([A-E](?:\s*,\s*[A-E])*)/);
      if (!m) return;
      questoes.push({ ul: alternativas, details: resposta, certas: m[1].split(/\s*,\s*/), escolhidas: [], feita: false, acertou: false });
    });
    if (questoes.length) {
      var placar = criar("div", "ferramentas");
      var texto = criar("span");
      var recomecar = criar("button", null, "Recomeçar");
      recomecar.type = "button";
      placar.appendChild(texto); placar.appendChild(recomecar);
      placar.appendChild(criar("small", "aviso-questao", "Clique numa alternativa para responder."));
      var h1 = document.querySelector("#conteudo h1");
      h1.parentNode.insertBefore(placar, h1.nextSibling);
      var atualizarPlacar = function () {
        var feitas = questoes.filter(function (q) { return q.feita; });
        var acertos = feitas.filter(function (q) { return q.acertou; }).length;
        texto.textContent = "Respondidas: " + feitas.length + " de " + questoes.length + " · Acertos: " + acertos +
          (feitas.length ? " (" + Math.round(100 * acertos / feitas.length) + "%)" : "");
      };
      var letra = function (li) { var m = li.textContent.trim().match(/^([A-E])\)/); return m ? m[1] : null; };
      questoes.forEach(function (q) {
        q.ul.classList.add("alternativas");
        if (q.certas.length > 1) {
          var aviso = criar("p", "aviso-questao", "Escolha " + q.certas.length + " alternativas.");
          q.ul.parentNode.insertBefore(aviso, q.ul);
        }
        Array.prototype.forEach.call(q.ul.children, function (li) {
          li.tabIndex = 0;
          li.setAttribute("role", "button");
          var escolher = function () {
            var l = letra(li);
            if (q.feita || !l || q.escolhidas.indexOf(l) >= 0) return;
            q.escolhidas.push(l);
            li.classList.add("marcada");
            if (q.escolhidas.length < q.certas.length) return;
            q.feita = true;
            q.acertou = q.escolhidas.every(function (x) { return q.certas.indexOf(x) >= 0; });
            q.ul.classList.add("respondida");
            Array.prototype.forEach.call(q.ul.children, function (outro) {
              var lo = letra(outro);
              outro.classList.remove("marcada");
              if (q.certas.indexOf(lo) >= 0) outro.classList.add("certa");
              else if (q.escolhidas.indexOf(lo) >= 0) outro.classList.add("errada");
            });
            q.details.open = true;
            atualizarPlacar();
          };
          li.addEventListener("click", escolher);
          li.addEventListener("keydown", function (e) { if (e.key === "Enter" || e.key === " ") { e.preventDefault(); escolher(); } });
        });
      });
      recomecar.addEventListener("click", function () {
        questoes.forEach(function (q) {
          q.feita = false; q.acertou = false; q.escolhidas = [];
          q.ul.classList.remove("respondida");
          Array.prototype.forEach.call(q.ul.children, function (li) { li.classList.remove("marcada", "certa", "errada"); });
          q.details.open = false;
        });
        atualizarPlacar();
        window.scrollTo(0, 0);
      });
      atualizarPlacar();
    }
  }

  // ---------- Flashcards em modo cartão ----------
  if (/\/flashcards\/(capitulo|dominio)-\d+\.html$/.test(caminho)) {
    var cards = Array.prototype.map.call(document.querySelectorAll("#conteudo details"), function (d) {
      var resumo = d.querySelector("summary");
      var resposta = d.cloneNode(true);
      resposta.removeChild(resposta.querySelector("summary"));
      return { pergunta: resumo.textContent.trim(), resposta: resposta.innerHTML };
    });
    if (cards.length) {
      var ferramentas = criar("div", "ferramentas");
      var estudar = criar("button", null, "Estudar em modo cartão");
      estudar.type = "button";
      ferramentas.appendChild(estudar);
      ferramentas.appendChild(criar("small", "aviso-questao", cards.length + " cartões, em ordem aleatória. Os que você errar voltam para o fim da fila."));
      var cabecalho = document.querySelector("#conteudo h1");
      cabecalho.parentNode.insertBefore(ferramentas, cabecalho.nextSibling);
      var cartao = criar("section", "cartao");
      cartao.hidden = true;
      cartao.setAttribute("aria-live", "polite");
      ferramentas.parentNode.insertBefore(cartao, ferramentas.nextSibling);

      var fila = [], acertos = 0, vistos = 0;
      var mostrar = function () {
        cartao.textContent = "";
        if (!fila.length) {
          cartao.appendChild(criar("p", "cartao-pergunta", "Fim! Você acertou de primeira " + acertos + " de " + cards.length + " cartões."));
          var denovo = criar("button", null, "Recomeçar");
          denovo.type = "button";
          denovo.addEventListener("click", comecar);
          var acoesFim = criar("div", "cartao-acoes"); acoesFim.appendChild(denovo); cartao.appendChild(acoesFim);
          return;
        }
        var c = fila[0];
        cartao.appendChild(criar("p", "cartao-info", "Faltam " + fila.length + " · vistos " + vistos));
        var face = criar("div", "cartao-face");
        face.tabIndex = 0;
        face.setAttribute("role", "button");
        face.appendChild(criar("div", "cartao-pergunta", c.pergunta));
        var dica = criar("small", "aviso-questao", "Pense na resposta e clique para virar.");
        face.appendChild(dica);
        cartao.appendChild(face);
        var acoes = criar("div", "cartao-acoes");
        var sei = criar("button", null, "Acertei"), naoSei = criar("button", null, "Errei, rever depois"), sair = criar("button", null, "Sair");
        [sei, naoSei, sair].forEach(function (b) { b.type = "button"; });
        sei.hidden = naoSei.hidden = true;
        acoes.appendChild(sei); acoes.appendChild(naoSei); acoes.appendChild(sair);
        cartao.appendChild(acoes);
        var virar = function () {
          if (face.querySelector(".cartao-resposta")) return;
          var r = criar("div", "cartao-resposta"); r.innerHTML = c.resposta;
          face.replaceChild(r, dica);
          sei.hidden = naoSei.hidden = false;
          sei.focus();
        };
        face.addEventListener("click", virar);
        face.addEventListener("keydown", function (e) { if (e.key === "Enter" || e.key === " ") { e.preventDefault(); virar(); } });
        sei.addEventListener("click", function () { if (!c.errou) acertos++; vistos++; fila.shift(); mostrar(); });
        naoSei.addEventListener("click", function () { c.errou = true; vistos++; fila.push(fila.shift()); mostrar(); });
        sair.addEventListener("click", function () { cartao.hidden = true; estudar.hidden = false; });
        face.focus();
      };
      var comecar = function () {
        fila = cards.map(function (c) { return { pergunta: c.pergunta, resposta: c.resposta, errou: false }; });
        for (var i = fila.length - 1; i > 0; i--) { var j = Math.floor(Math.random() * (i + 1)); var t = fila[i]; fila[i] = fila[j]; fila[j] = t; }
        acertos = 0; vistos = 0;
        cartao.hidden = false; estudar.hidden = true;
        mostrar();
      };
      estudar.addEventListener("click", comecar);
    }
  }
})();
