from pathlib import Path

def generate_email_template(form_id, variables) -> Path:
    email_template = ""
    
    if form_id == 1:
        email_template = f"""
            Assunto: Proposta e-Auditoria para {variables.get("nome")} (Válida por 1 dia útil)
 
            Corpo do e-mail:
            Olá {variables.get("enviou")}, tudo bem?
            
            Conforme conversamos, preparei a proposta completa da plataforma líder em auditoria tributária do Brasil para automatizar a correção dos seus SPEDs — com resultados imediatos em produtividade, segurança fiscal e geração de caixa.
            
            🔍 O que você vai encontrar na proposta anexa:
            
            ✅ {variables.get("erros")} erros do SPED corrigidos automaticamente em apenas 2 minutos
            ✅ Log de correções completo em PDF com sua logo — pronto para enviar ao cliente
            ✅ Redução de até 98% no tempo de correção dos arquivos
            ✅ Prevenção de {variables.get("multa")} de multa prevista com base no arquivo da empresa {variables.get("cnpj")}
            ✅ Recuperação de créditos de ICMS esquecidos (inclusive no Simples Nacional)
            ✅ Correções validadas com base na legislação oficial e prontos para transmitir
            ✅ Vídeo de demonstração da ferramenta em apenas 1min23s
            
            🎯 Ganhos imediatos para o escritório {variables.get("nome")}:
            - Mais agilidade e escala para atender clientes do Lucro Real, Presumido e Simples Nacional
            - Eliminação de retrabalho manual e erros que geram autuações
            - Novo diferencial competitivo com relatórios que encantam o cliente
            - Mais previsibilidade, mais clientes, mais produtividade

            💰 Investimento com condições especiais (válidas por apenas 1 dia útil):
            - De {variables.get("valorsemdesc")} → por {variables.get("valorcomdesc")}
            - Implantação de R$ {variables.get("valorimplant")}
            - Fidelidade: {variables.get("fidelidade")}

            📌 Próximo passo: Assim que confirmar, ativamos sua conta e liberamos a ferramenta em minutos.
            
            {variables.get("enviou")} está a um clique de transformar os SPEDs em uma fonte de resultado — automatizando erros, ganhando tempo e aumentando a segurança fiscal.
            
            Fico à disposição para tirar dúvidas ou agendarmos um retorno rápido.
            No aguardo da sua confirmação!
            Forte abraço,

            {variables.get("vendedor")}
            Especialista em Soluções Fiscais

            📞 32-3212-4324
            www.e-auditoria.com.br
        """
    elif form_id == 2: 
        email_template = f"""
            Assunto: Proposta e-Auditoria para {variables.get("nome")} (Válida por 1 dia útil)
            
            Corpo do e-mail:
            Olá, tudo bem?
            
            Conforme conversamos, preparei a proposta completa da plataforma líder em auditoria tributária do Brasil para automatizar a correção dos seus SPEDs — com resultados imediatos em produtividade, segurança fiscal e geração de caixa.
            
            🔍 O que você vai encontrar na proposta anexa:
            
            ✅ Como corrigir erros do SPED automaticamente em apenas 2 minutos
            ✅ Redução de até 98% no tempo de correção dos arquivos
            ✅ Prevenção de multa prevista com base no arquivo da empresa
            ✅ Recuperação de créditos de ICMS esquecidos (inclusive no Simples Nacional)
            ✅ Correções validadas com base na legislação oficial e prontos para transmitir
            ✅ Vídeo de demonstração da ferramenta em apenas 1min23s
            
            🎯 Ganhos imediatos para o escritório {variables.get("nome")}:
            - Mais agilidade e escala para atender clientes do Lucro Real, Presumido e Simples Nacional
            - Eliminação de retrabalho manual e erros que geram autuações
            - Novo diferencial competitivo com relatórios que encantam o cliente
            - Mais previsibilidade, mais clientes, mais produtividade

            💰 Investimento com condições especiais (válidas por apenas 1 dia útil):
            - De {variables.get("valorsemdesc")} → por {variables.get("valorcomdesc")}
            - Implantação de R$ {variables.get("valorimplant")}
            - Fidelidade: {variables.get("fidelidade")}

            📌 Próximo passo: Assim que confirmar, ativamos sua conta e liberamos a ferramenta em minutos.
            
            Você está a um clique de transformar os SPEDs em uma fonte de resultado — automatizando erros, ganhando tempo e aumentando a segurança fiscal.
            
            Fico à disposição para tirar dúvidas ou agendarmos um retorno rápido.
            No aguardo da sua confirmação!
            Forte abraço,

            {variables.get("vendedor")}
            Especialista em Soluções Fiscais

            📞 32-3212-4324 
            www.e-auditoria.com.br
        """
    elif form_id == 3:
        email_template = f"""
            Assunto: Proposta e-Auditoria para {variables.get("nome")} (Válida por 1 dia útil)
 
            Corpo do e-mail:
            Olá {variables.get("enviou")}, tudo bem?
            
            Conforme conversamos, preparei a proposta completa da plataforma líder em auditoria tributária do Brasil para automatizar a correção dos seus SPEDs — com resultados imediatos em produtividade, segurança fiscal e geração de caixa.
            
            🔍 O que você vai encontrar na proposta anexa:
            
            ✅ {variables.get("erros")} erros do SPED corrigidos automaticamente em apenas 2 minutos
            ✅ Log de correções completo em PDF com sua logo — pronto para enviar ao cliente
            ✅ Redução de até 98% no tempo de correção dos arquivos
            ✅ Prevenção de {variables.get("multa")} de multa prevista com base no arquivo da empresa {variables.get("cnpj")}
            ✅ Recuperação de créditos de ICMS esquecidos (inclusive no Simples Nacional)
            ✅ Correções validadas com base na legislação oficial e prontos para transmitir
            ✅ Vídeo de demonstração da ferramenta em apenas 1min23s
            
            🎯 Ganhos imediatos para o escritório {variables.get("nome")}:
            - Mais agilidade e escala para atender clientes do Lucro Real, Presumido e Simples Nacional
            - Eliminação de retrabalho manual e erros que geram autuações
            - Novo diferencial competitivo com relatórios que encantam o cliente
            - Mais previsibilidade, mais clientes, mais produtividade

            💰 Investimento com condições especiais (válidas por apenas 1 dia útil):

            Plano Atual: {variables.get("planoold")}
            Valor: {variables.get("valorsemdescold")}

            Plano da Proposta: {variables.get("plano")}
            Valor: {variables.get("valorsemdesc")}


            - Implantação de R$ {variables.get("valorimplant")}
            - Fidelidade: {variables.get("fidelidade")}

            📌 Próximo passo: Assim que confirmar, ativamos sua conta e liberamos a ferramenta em minutos.
            
            {variables.get("enviou")} está a um clique de transformar os SPEDs em uma fonte de resultado — automatizando erros, ganhando tempo e aumentando a segurança fiscal.
            
            Fico à disposição para tirar dúvidas ou agendarmos um retorno rápido.
            No aguardo da sua confirmação!
            Forte abraço,

            {variables.get("vendedor")}
            Especialista em Soluções Fiscais

            📞 32-3212-4324
            www.e-auditoria.com.br
        """
    elif form_id == 4:
        email_template = f"""
            Assunto: Proposta e-Auditoria para {variables.get("nome")} (Válida por 1 dia útil)
    
            Corpo do e-mail:
            Olá, tudo bem?
            
            Conforme conversamos, preparei a proposta completa da plataforma líder em auditoria tributária do Brasil para automatizar a correção dos seus SPEDs — com resultados imediatos em produtividade, segurança fiscal e geração de caixa.
            
            🔍 O que você vai encontrar na proposta anexa:
            
            ✅ Como corrigir erros do SPED automaticamente em apenas 2 minutos
            ✅ Redução de até 98% no tempo de correção dos arquivos
            ✅ Prevenção de multa prevista com base no arquivo da empresa
            ✅ Recuperação de créditos de ICMS esquecidos (inclusive no Simples Nacional)
            ✅ Correções validadas com base na legislação oficial e prontos para transmitir
            ✅ Vídeo de demonstração da ferramenta em apenas 1min23s
            
            🎯 Ganhos imediatos para o escritório {variables.get("nome")}:
            - Mais agilidade e escala para atender clientes do Lucro Real, Presumido e Simples Nacional
            - Eliminação de retrabalho manual e erros que geram autuações
            - Novo diferencial competitivo com relatórios que encantam o cliente
            - Mais previsibilidade, mais clientes, mais produtividade

            💰 Investimento com condições especiais (válidas por apenas 1 dia útil):

            Plano Atual: {variables.get("planoold")}
            Valor: {variables.get("valorsemdescold")}

            Plano da Proposta: {variables.get("plano")}
            Valor: {variables.get("valorsemdesc")}


            - Implantação de R$ {variables.get("valorimplant")}
            - Fidelidade: {variables.get("fidelidade")}

            📌 Próximo passo: Assim que confirmar, ativamos sua conta e liberamos a ferramenta em minutos.
            
            Você está a um clique de transformar os SPEDs em uma fonte de resultado — automatizando erros, ganhando tempo e aumentando a segurança fiscal.
            
            Fico à disposição para tirar dúvidas ou agendarmos um retorno rápido.
            No aguardo da sua confirmação!
            Forte abraço,

            {variables.get("vendedor")}
            Especialista em Soluções Fiscais

            📞 32-3212-4324 
            www.e-auditoria.com.br
        """

    return email_template