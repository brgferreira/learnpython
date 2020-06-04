#!/usr/bin/env python
# coding: utf-8

# # Primeiros Exemplos

# In[3]:


print('PrimeiroPrograma')
1 + 2 + 3
4 + 5 + 6


# In[4]:


print(1 + 2 + 3)
print(4 + 5 + 6)


# In[5]:


print(True)
print(False)
print(1.2 +2)


# In[6]:


print('Aqui usei aspas simples')
print("aqui usei aspas duplas")
print('Você é ' +3 * 'muito ' + 'Legal!')


# # Exemplo Lista / Dicionario

# In[7]:


lista = [1, 2, 3]
dicionario = {'Nome': 'Pedro', 'Idade': 22}


# In[8]:


print([1 , 2, 3])
print({'Nome': 'Joao', 'Idade': 22})
print(None)


# # Operadores Aritméticos - Aula 26

# In[6]:


print (2 + 3)
print (4 - 7)
print (2 * 5.3)
print (9.4 / 3)
print (9.4 // 3) # // força o numero a ser inteiro ou seja um float inteiro
print (2 ** 8) # ** eleva a potencia
print (10 % 3) # % pega o resto da divisão

a = 12
b = a
print (a + b)


# # Desafio Aula 27 

# In[14]:


# Minhas variáveis - Resposta
salario = 3450.45
despesas = 2456.2

porc = despesas / salario
print (porc * 100)

# Resposta do Desafio
percentual_comprometido = despesas / salario * 100
percentual_comprometido


# # Operadores Relacionais

# In[18]:


# comparação de "igualdade"
3 > 4
4 >= 3
1 < 2
3 <= 1
3 != 2
3 == '3'


# # Operadores de Atribuição

# In[40]:


# Variavel e um local de memoria rotulado
a = 3
a = a + 7
print (a)

#a = 5
a += 5 # a = a + 5
print (a)

a -= 3
print (a)
a *= 2
print (a)

a/= 4
print (a)

a %= 4
print (a)

a **= 8
print (a)

a //= 256
print(a)


# # Operadores Lógicos

# In[68]:


True or False
7 != 3 and 2 > 3

# Tabela verdade do AND
True and True
True and False
False and True
False and False

True and True and False and True and True and True and True 

# Tabela Verdade do OR
True or True
True or False
False or True
False or False
False or False or True or False or False or False

# Tabela verdade do XOR
True != True
True != False
False != True
False != False

# Operador de Negação (unário)
not True
not False

not 0
not 1
not not -1
not True
not not True

# Cuidado!
True & True
False | True
True ^ False

# AND Bit-a-bit
# 3 = 11 
# 2 = 10
3 & 2

# XOR Bit-a-bit
# 3 = 11
# 2 = 10
# _ = 11
3 | 2

# In[68]:

# Um pouco de realidade

saldo = 1000
salario = 4000
despesas = 2967

saldo_positivo = saldo > 0
despesas_controladas = salario - despesas >= 0.2 * salario
meta =  saldo_positivo and despesas_controladas
meta


# In[74]:

# # Desafio Operadores Logicos - Aula 32

# Desafio Operadores Lógicos

# Trabalhos

"""
- Confirmando os 2 trabalhos: compra uma TV 50' + Sorvete
- Confirmando apenas 1 trabalho: compra TV 32' + Sorvete
- Nenhum confirmado: Fica em casa e nao toma sorvete
"""
trabalho_terca = True
trabalho_quinta = False

tv_50 = trabalho_terca and trabalho_quinta
sorvete = trabalho_terca or trabalho_quinta
tv_34 = trabalho_terca != trabalho_quinta #XOR
mais_saudavel = not sorvete

print("TV50={} TV32={} Sorvete={} Saudavel={}".format(tv_50, tv_34, sorvete,mais_saudavel ))


# %%

## Operadores Unários

a = 3
-a
+a
not 0
not 1
not -2
not False
not not True


# %%

## Operadores Ternários

esta_chuvendo = True
print ('hoje estou com as roupas ' + ('Secas.', 'Molhadas.')[esta_chuvendo])

print ('hoje estou com as roupas ' + ('molhadas.' if esta_chuvendo else 'secas.'))
# %%

