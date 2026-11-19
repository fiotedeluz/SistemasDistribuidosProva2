segue aqui registro do terminal da prava pratica

o terminal registrado esta dentro do workspace fornecido pelo proprio github

. registro do codigo funcionando apos transcrição do papel
"
@fiotedeluz ➜ /workspaces/SistemasDistribuidosProva2 (main) $ python --version
Python 3.14.2
@fiotedeluz ➜ /workspaces/SistemasDistribuidosProva2 (main) $ ^C
@fiotedeluz ➜ /workspaces/SistemasDistribuidosProva2 (main) $ python central_pedidos.py 
=== CENTRAL DE PEDIDOS ===
Limite simultaneo: 3
estoque inicial: 10
Pedidos Confirmados: [101, 102, 103]
estoque principal: 7
replica antes: 10
replica depois: 10
consulta apos a falha: INDISPONIVEL None
@fiotedeluz ➜ /workspaces/SistemasDistribuidosProva2 (main) $ 
"

. e segue registro apos feitas as correções
"
@fiotedeluz ➜ /workspaces/SistemasDistribuidosProva2 (main) $ python central_pedidos.py 
=== CENTRAL DE PEDIDOS ===
Limite simultaneo: 2
estoque inicial: 10
Pedidos Confirmados: [101, 102, 103]
estoque principal: 7
replica antes: 10
replica depois: 7
consulta apos a falha: REPLICA 7
@fiotedeluz ➜ /workspaces/SistemasDistribuidosProva2 (main) $ 
"

Para alcançar esse resultado algumas mudanças tiveram q ser feitas

. primeiro a variavel "MAXIMO_SIMULTANEO" foi alterada de 3 para 2
. segundo para que a atualização ocorresse autometicamente alterei a variavel usada, antes o sistema atualizada de principal para principal mas precisamos que a replica fique igual a principal
. e terceiro a seção consultar estoque estava consultando o estoque principal duas veses da mesma forma, fiz a alteração para consultar se o sistema principal estava ativado, em caso de ele não estar (a condição online estiver 'False') o sistema le a replica para que apenas se as duas tentativas falharem ele retorne falha total
. e por fim acima vemos a validação do sistema todo funcionando

