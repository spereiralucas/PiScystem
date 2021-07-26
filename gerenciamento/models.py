from django.db import models


# Banco de dados - tabela de cadastramento de espécie
class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):  # Define qual item da tabela é exibido na consulta
        return self.nome


# Banco de dados - tabela de cadastramento de tanques
class Tanque(models.Model):
    id = models.IntegerField.auto_creation_counter
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    observacoes = models.TextField(null=True, blank=True)

    def __int__(self):
        return self.id


# Banco de dados - tabela de aferição rotineira
class Afericao(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    data = models.DateTimeField(auto_now_add=True)  # Adiciona a data atual sem que o usuário interfira no dado
    quantidade_aferida = models.IntegerField(max_length=10, null=False)
    quantidade_aproximada = models.IntegerField(max_length=10, null=False)
    peso = models.DecimalField(max_digits=7, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    # racao_diaria = models.DecimalField(peso/quantidade_aferida)
    observacoes = models.TextField(null=True, blank=True)  # Permitindo que este campo possa ser deixado em branco

    class Meta:  # Altera os nomes das classes para que o usuário as veja escritas corretamente
        verbose_name_plural = "Aferições"

    def __int__(self):
        return self.id
