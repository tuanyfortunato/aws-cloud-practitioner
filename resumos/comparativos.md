# Comparativos de Serviços

| A | B | Diferença principal |
|---|---|---|
| CloudWatch | CloudTrail | CloudWatch = métricas, logs e alarmes (desempenho); CloudTrail = quem fez qual chamada de API (auditoria) |
| Security Group | Network ACL | SG = nível de instância, stateful, só regras de permissão; NACL = nível de sub-rede, stateless, permite e nega |
| SQS | SNS | SQS = fila (pull, desacoplamento); SNS = pub/sub (push para vários assinantes) |
| EBS | EFS | EBS = bloco, ligado a uma instância em uma AZ; EFS = arquivos (NFS), compartilhado entre várias instâncias e AZs |
| RDS | DynamoDB | RDS = relacional (SQL); DynamoDB = NoSQL chave-valor, serverless |
| Shield | WAF | Shield = proteção DDoS; WAF = filtra requisições web (SQL injection, XSS) |
| Inspector | GuardDuty | Inspector = vulnerabilidades em EC2/ECR/Lambda; GuardDuty = detecção de ameaças por análise de logs |
| Cost Explorer | Budgets | Cost Explorer = analisa gastos passados e previsão; Budgets = alertas quando passar de um limite |
|  |  |  |
