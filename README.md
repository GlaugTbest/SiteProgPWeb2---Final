Visão geral

Aplicação de um sistema simples de agendamento de salas, desenvolvido com Django, com o objetivo de demonstrar o funcionamento de um servidor web local acessível por outros dispositivos na mesma rede.

O sistema permite que usuários visualizem reservas existentes, criem novas reservas e removam reservas já cadastradas, tudo por meio de uma interface web simples e funcional.

Tecnologias utilizadas

Python 3

Django

HTML + CSS (templates Django)

Servidor de desenvolvimento do Django

Banco de dados SQLite (padrão do Django)

Não são utilizados servidores externos ou serviços em nuvem. Toda a aplicação roda localmente.

Funcionamento do servidor

O servidor é executado utilizando o servidor de desenvolvimento nativo do Django (manage.py runserver), configurado para escutar em 0.0.0.0, permitindo que outros dispositivos da mesma rede local acessem a aplicação utilizando o IP da máquina que está hospedando o servidor.

Exemplo de acesso:

http://192.168.0.10:8000


Dessa forma, qualquer computador ou celular conectado à mesma rede consegue acessar a aplicação pelo navegador, sem necessidade de configurações no roteador ou uso de serviços externos.

Funcionalidades principais:

📅 Listagem de reservas cadastradas

➕ Criação de novas reservas de sala

❌ Remoção de reservas existentes

🎯 Interface simples e objetiva

🌐 Acesso pela rede local via IP



A aplicação foi desenvolvida como parte da disciplina Programação para Web II, com foco em:

Criação de aplicações web com Django

Funcionamento de servidores web locais

Comunicação cliente-servidor

Acesso via rede local

Estrutura básica de um projeto web funcional
