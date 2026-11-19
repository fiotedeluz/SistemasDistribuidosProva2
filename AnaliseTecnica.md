segue as respostas para questões da analise tecnica

1. o semaforo funciona para impedir que pedidos sejam feitos simultaneamente para que o servidor possa processar corretamente e individualmente
2. nessa situação a 'replica' esta funcionando como um backup, registrando o estoque de 'principal', caso ocorra uma falha precisamos que a replica esteja atualizada e possa fornecer uma informação correta sobreultimo estado da 'principal'. para isso ela precisa estar sincronizada
3. tolerancia de falhas significa preparar o sistema para possiveis catastrofes, varios erros podem ocorrer durante o funcionamento de um sistema e preparar tolerancia a falhas significa possuir previamente respostas para erros previstos
4. o lock impede processamento simultaneo de recursos para que o arquivo faça o caminho esperado e não trave o sistema em um caso de concorrencia por recursos interdependentes
5. depois, se a replica fosse sincronizada com o estado anterior a mudança ela sempre estaria oblivia a mudança mais atual estando desatualizada e incorreta
