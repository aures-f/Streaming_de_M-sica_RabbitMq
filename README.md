# 🎵 Sistema Distribuído de Streaming de Música

**Trabalho Final da Disciplina de Sistemas Distribuídos**  
Curso: Análise e Desenvolvimento de Sistemas  
Universidade Federal do Ceará (UFC)

**Dupla:**  
- Aurelice Freitas  
- José Talyson  

---

## 📌 Descrição do Projeto

Este projeto implementa um **sistema distribuído inspirado em plataformas de streaming de música**, como Spotify e Deezer, com foco na **arquitetura distribuída**, comunicação entre processos e uso de middleware.

O objetivo é demonstrar, na prática, os principais conceitos estudados na disciplina de **Sistemas Distribuídos**, como:

- Comunicação síncrona (RPC)
- Comunicação assíncrona
- Comunicação indireta
- Uso de Gateway (Middleware)
- Uso de Broker de Mensagens (RabbitMQ)
- Execução de serviços em processos separados

A interface gráfica **não é prioridade**, pois o foco é a arquitetura e a comunicação entre os componentes.

---

## 🧩 Arquitetura do Sistema

O sistema é composto por quatro tipos de componentes:

### 1️⃣ Cliente (`client.py`)
Simula ações do usuário, como:
- Buscar músicas
- Criar playlists
- Reproduzir músicas

O cliente **não acessa diretamente os serviços**, apenas o Gateway.

---

### 2️⃣ Gateway / Middleware (`gateway.py`)
É o **ponto único de entrada** do sistema.

Responsabilidades:
- Receber requisições do cliente
- Encaminhar para o serviço correto
- Coordenar chamadas RPC
- Publicar eventos assíncronos no RabbitMQ

---

### 3️⃣ Serviços Distribuídos (`services/`)
Cada serviço roda em um **processo separado**:

- `catalogo_service.py` → Busca de músicas  
- `playlist_service.py` → Gerenciamento de playlists  
- `usuario_service.py` → Histórico de reproduções  

---

### 4️⃣ Broker de Mensagens
Utiliza **RabbitMQ** para:
- Comunicação indireta
- Comunicação assíncrona
- Processamento de eventos

---

## 🔁 Tipos de Comunicação

| Tipo | Onde ocorre |
|------|------------|
| RPC (síncrona) | Cliente → Gateway → Serviços |
| Indireta | Gateway → RabbitMQ → Serviço de Usuário |
| Assíncrona | Eventos de reprodução de música |

---

## 📂 Estrutura do Projeto

```text
trabalhofinal/
│
├── client.py
├── gateway.py
├── messaging.py
├── requirements.txt
├── README.md
│
└── services/
├── catalogo_service.py
├── playlist_service.py
└── usuario_service.py

```
---

## 🛠 Tecnologias Utilizadas

- Python 3.x
- RabbitMQ
- Biblioteca `pika`
- Sockets TCP

---

## ▶️ Como Executar

### 1. Ativar o ambiente virtual
```bash
caminho_do_venv/Scripts/activate
```

### 2. Instalar dependências
```bash
pip install -r requirements.txt
```
### 3. Executar os serviços (em terminais separados)
```bash
python services/catalogo_service.py
python services/playlist_service.py
python services/usuario_service.py
python gateway.py
```

### 4. Executar o cliente
```bash
python client.py
```

## Conclusão

O desenvolvimento deste projeto permitiu aplicar, na prática, os principais conceitos estudados na disciplina de **Sistemas Distribuídos**, como a divisão do sistema em serviços independentes, a comunicação entre processos e o uso de um **middleware (Gateway)** para centralizar e coordenar as requisições.

A utilização do **RabbitMQ** possibilitou a implementação de comunicação **assíncrona e indireta**, enquanto as chamadas via **RPC** garantiram a comunicação síncrona entre o cliente, o gateway e os serviços. Dessa forma, o sistema demonstra claramente como diferentes componentes podem cooperar em um ambiente distribuído.

Mesmo sendo uma simulação simples de uma plataforma de streaming de música, o projeto cumpre seu papel ao representar um cenário realista de sistemas distribuídos, destacando a importância da organização, da escalabilidade e da confiabilidade na troca de informações entre os módulos.

Por fim, o trabalho atendeu integralmente aos requisitos propostos pela disciplina, consolidando o aprendizado teórico por meio de uma implementação prática e funcional.
