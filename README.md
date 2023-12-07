# Chatbot de primeira matrícula FATEC

## O projeto

Decidi criar esse chatbot para automatizar os procedimentos de matrícula na FATEC devido à obsolescência do sistema atual, que utiliza o envio de processos por e-mail. O método manual, que requer a disponibilidade de funcionários para análise de documentos e envio de respostas, torna-se demorado. A automatização, por meio de um chatbot, agiliza e simplifica o processo. Os alunos podem realizar a matrícula 24 horas por dia, sete dias por semana, sem depender do horário de atendimento da FATEC. Além disso, oferece uma experiência mais intuitiva, possibilitando uma matrícula mais rápida e eficiente.

***

## Desenvolvimento do projeto

O desenvolvimento do projeto foi na linguagem [Python](https://www.python.org/doc/), também fazendo uso do [Serverless](https://www.serverless.com/framework/docs) e do [Twilio](https://www.twilio.com/docs/whatsapp). Além de contar com a utilização dos seguintes serviços AWS: `Amazon Lex`, `Amazon Rekognition`, `Amazon Transcribe`, `Amazon S3`, `AWS Lambda`, `Amazon DynamoDB` e `Amazon CloudWatch`.

***

## Diagrama de fluxo de informação
<div aling="center">
    <img src="./public/fluxoDeInformacoes.png" width="1000px"/>
</div>

***

## Arquitetura
<div aling="center">
    <img src="./public/arquitetura_final.jpg" width="1000px"/>
</div>

***

## Estrutura de pastas
```shell
├─ friday_lambda/
│   ├─ src/
│   │   ├─ aws/
│   │   │   ├─ dynamo_functions/
│   │   │   │   └─ get_item_on_approved.py
│   │   │   │   └─ get_item_on_matriculation.py
│   │   │   │   └─ put_item.py
│   │   │   ├─ lex/
│   │   │   │   └─ consultar_matricula.py
│   │   │   │   └─ fazer_matricula.py
│   │   │   ├─ rekognition_functions/
│   │   │   │   └─ compare_faces.py
│   │   │   │   └─ detect_cpf.py
│   │   │   └─ clients.py
│   │   └─ utils/
│   │       └─ validate_cpf.py
│   │
│   └─ lambda_function.py
│
├─ friday_orchestrator/
│   ├─ aws/
│   │   ├─ lex/
│   │   │   └─ get_lex_response.py
│   │   ├─ s3/
│   │   │   └─ upload_audio.py
│   │   │   └─ upload_image.py
│   │   ├─ transcribe/
│   │   │   └─ get_text.py
│   │   └─ clients.py
│   ├─ twilio/
│   │   └─ create_message.py
│   │   └─ twilio_client.py
│   ├─ utils/
│   │   └─ env_class.py
│   │   └─ get_media.py
│   │   
│   └─ handler.py
│
├─ public/
│   └─ arquitetura_final.jpg
│   └─ fluxoDeInformacoes.png
│
└─ .env.example
└─ .gitignore
└─ README.md
└─ package.json
└─ requirements.txt
└─ serverless.yml
└─ setup.py
```

***


## Dificuldades encontradas

* **Dificuldade**: Fazer o upload da mídia enviada pelo usuário no s3.
* *Solução*: Leitura da documentação do [Twilio](https://www.twilio.com/docs/usage/requests-to-twilio).

* **Dificuldade**: Trabalhar com a lógica do codehook no Lex.
* *Solução*: Consultar a documentação do [Lex](https://docs.aws.amazon.com/lexv2/latest/dg/lambda.html) e usar a criatividade

***