# SPDX-FileCopyrightText: Copyright (c) 2024 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

### Markdown usado para renderizar certa documentação na aplicação gradio. ###

setup = """
Bem-vindo ao projeto de exemplo Hybrid RAG para o NVIDIA AI Workbench! \n\nPara começar, clique no botão a seguir para configurar o servidor de API de backend e o banco de dados vetorial. Este é um processo único e pode levar alguns momentos para ser concluído.
"""

update_kb_info = """
<br> 
Carregue seus arquivos de texto aqui. Eles serão incorporados no banco de dados vetorial e persistirão como contexto potencial para o modelo até você limpar o banco de dados. Cuidado, limpar o banco de dados é irreversível!
"""

inf_mode_info = "Para usar um endpoint na NUVEM para inferência, selecione o modelo desejado antes de fazer uma consulta."

local_info = """
Primeiro, selecione o modelo desejado e o nível de quantização. Você pode, opcionalmente, filtrar a lista de modelos por modelos restritos e não restritos. Em seguida, carregue o modelo. Isso pode baixá-lo ou carregá-lo do cache. O download pode levar alguns minutos, dependendo da sua rede.

Uma vez que o modelo esteja carregado, inicie o Servidor de Inferência. Geralmente, leva cerca de 40 segundos para ser iniciado. Certifique-se de ter VRAM suficiente na GPU para rodar um modelo localmente ou poderá ocorrer erro de memória (OOM) ao iniciar o servidor de inferência. Quando o servidor for iniciado, converse com o modelo usando o campo de texto à esquerda.
"""

local_prereqs = """
* Um segredo de projeto ``HUGGING_FACE_HUB_TOKEN`` é necessário para modelos restritos. Veja [Tutorial 1](https://github.com/NVIDIA/workbench-example-hybrid-rag/blob/main/README.md#tutorial-1-using-a-local-gpu). 
* Se estiver usando qualquer um dos seguintes modelos restritos, verifique se "Você foi autorizado a acessar este modelo" aparece na página do modelo:
    * [Mistral-7B-Instruct-v0.1](https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.1)
    * [Mistral-7B-Instruct-v0.2](https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.2)
    * [Llama-2-7b-chat-hf](https://huggingface.co/meta-llama/Llama-2-7b-chat-hf)
    * [Llama-3-8B-Instruct](https://huggingface.co/meta-llama/Meta-Llama-3-8B-Instruct)
"""

local_trouble = """
* Certifique-se de ter parado quaisquer processos locais também rodando nas GPUs do sistema. Caso contrário, poderá ocorrer erro de memória (OOM) ao rodar no servidor de inferência local. 
* Sua chave do Hugging Face pode estar ausente ou sem permissões para certos modelos. Verifique se você vê "Você foi autorizado a acessar este modelo" em cada página:
    * [Mistral-7B-Instruct-v0.1](https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.1)
    * [Mistral-7B-Instruct-v0.2](https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.2)
    * [Llama-2-7b-chat-hf](https://huggingface.co/meta-llama/Llama-2-7b-chat-hf)
    * [Llama-3-8B-Instruct](https://huggingface.co/meta-llama/Meta-Llama-3-8B-Instruct)
"""

cloud_info = """
Este método utiliza Endpoints da API NVCF do Catálogo de APIs da NVIDIA. Selecione a família de modelos desejada e o modelo a partir do menu suspenso. Você pode então consultar o modelo usando o campo de texto à esquerda.
"""

cloud_prereqs = """
* Um segredo de projeto ``NVCF_RUN_KEY`` é necessário. Veja o [Quickstart](https://github.com/NVIDIA/workbench-example-hybrid-rag/blob/main/README.md#tutorial-using-a-cloud-endpoint). 
    * Gere a chave [aqui](https://build.nvidia.com/mistralai/mistral-7b-instruct-v2) clicando em "Get API Key". Faça login com as [credenciais NGC](https://ngc.nvidia.com/signin).
"""

cloud_trouble = """
* Certifique-se de que sua chave NVCF esteja correta e configurada adequadamente no AI Workbench. 
"""

nim_info = """
Este método utiliza um [container NIM](https://catalog.ngc.nvidia.com/orgs/nim/teams/meta/containers/llama3-8b-instruct/tags) que você pode optar por hospedar por conta própria em sua infraestrutura de sua escolha. Confira a documentação do NIM [aqui](https://docs.nvidia.com/nim/large-language-models/latest/getting-started.html) para mais detalhes. Os usuários também podem tentar serviços de terceiros que suportem a [API OpenAI](https://github.com/ollama/ollama/blob/main/docs/openai.md) como o [Ollama](https://github.com/ollama/ollama/blob/main/README.md#building). Digite o IP do microserviço desejado, número da porta opcional e o nome do modelo sob a opção de Microserviço Remoto. Em seguida, inicie a conversa usando o campo de texto à esquerda.

Para usuários do AI Workbench no DOCKER, você também pode optar por executar uma instância NIM *localmente* no sistema, expandindo a opção "Microserviço Local"; certifique-se de que quaisquer outros processos locais de GPU tenham sido parados primeiro para evitar problemas de memória. O container ``llama3-8b-instruct`` do NIM é fornecido como fluxo padrão. Busque o container NIM desejado, selecione "Start Microservice" e inicie a conversa quando o processo estiver completo.
"""

nim_prereqs = """
* (Remoto) Configure um NIM em outro sistema ([documentação](https://docs.nvidia.com/nim/large-language-models/latest/getting-started.html)). Alternativamente, você pode configurar um serviço de terceiros que suporte a [API OpenAI](https://github.com/ollama/ollama/blob/main/docs/openai.md) como o [Ollama](https://github.com/ollama/ollama/blob/main/README.md#building). Certifique-se de que seu serviço esteja em execução e acessível. Veja o [Tutorial 2](https://github.com/NVIDIA/workbench-example-hybrid-rag/blob/main/README.md#tutorial-2-using-a-remote-microservice). 
* (Local) AI Workbench rodando no DOCKER é necessário para a opção LOCAL NIM. Leia e siga os pré-requisitos e configurações adicionais no [Tutorial 3](https://github.com/NVIDIA/workbench-example-hybrid-rag/blob/main/README.md#tutorial-3-using-a-local-microservice).
"""

nim_trouble = """
* Envie uma solicitação curl para seu microserviço para garantir que ele esteja em execução e acessível. Documentação do NIM [aqui](https://docs.nvidia.com/nim/large-language-models/latest/getting-started.html).
* AI Workbench rodando em runtime Docker é necessário para a opção LOCAL NIM. Caso contrário, configure o NIM auto-hospedado para ser usado remotamente. 
* Se estiver usando a opção NIM local, certifique-se de que configurou os parâmetros de projeto adequados de acordo com o README deste projeto. Ao contrário dos outros modos de inferência, esses não são pré-configurados. 
* Se houver outros processos rodando na(s) GPU(s) local(is), você poderá enfrentar problemas de memória ao rodar o NIM localmente. Pare os outros processos.
"""

num_token_label = """
O número máximo de tokens que podem ser gerados na conclusão.
"""

temp_label = """
Qual temperatura de amostragem usar, entre 0 e 2. Valores mais altos, como 0.8, tornarão a saída mais aleatória, enquanto valores mais baixos, como 0.2, tornarão a saída mais focada e determinística. Recomendamos alterar este parâmetro ou top_p, mas não ambos.
"""

top_p_label = """
Uma alternativa à amostragem com temperatura, chamada amostragem por núcleo, onde o modelo considera os resultados dos tokens com massa de probabilidade top_p. Então, 0.1 significa que apenas os tokens que compõem os 10% principais da massa de probabilidade serão considerados.
"""

freq_pen_label = """
Número entre -2.0 e 2.0. Valores positivos penalizam novos tokens com base na frequência existente no texto até o momento, diminuindo a probabilidade do modelo de repetir a mesma linha literalmente.
"""

pres_pen_label = """
Número entre -2.0 e 2.0. Valores positivos penalizam novos tokens com base em sua aparição no texto até o momento, aumentando a probabilidade do modelo de falar sobre novos tópicos.
"""
