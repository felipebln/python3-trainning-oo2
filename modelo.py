class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    def dar_likes(self):
        self._likes += 1

    @property
    def likes(self):
        return self._likes

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome

    def __str__(self):
        return f'{self.nome} - {self.ano} - {self._likes}'


class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    # metodo magico top
    def __str__(self):
        return f'{self.nome} - {self.ano} - {self.duracao} min - {self._likes}'


class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f'{self.nome} - {self.ano} - {self.temporadas} temporadas - {self._likes}'


class Playlist:
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas

    # Metodo magico top
    def __getitem__(self, item):
        return self._programas[item]

    @property
    def listagem(self):
        return self._programas

    def __len__(self):
        return len(self._programas)


vingadores = Filme('vingadores - guerra infinita', 2018, 160)
atlanta = Serie('atlanta', 2018, 2)
tmep = Filme('todo mundo em panico', 1999, 100)
demolidor = Serie('demolidor', 2017, 2)

vingadores.dar_likes()
vingadores.dar_likes()
vingadores.dar_likes()

tmep.dar_likes()
tmep.dar_likes()
tmep.dar_likes()
tmep.dar_likes()
demolidor.dar_likes()

atlanta.dar_likes()

filmes_e_serires = [vingadores, atlanta, demolidor, tmep]

playlist_fim_de_semana = Playlist('Fim de semana', filmes_e_serires)

print(f'Tamanho do Playlist: {len(playlist_fim_de_semana)}')

for programa in playlist_fim_de_semana:
    print(programa)

print(f'Demolidor Esta ou não na playlists? '
      f'{demolidor in playlist_fim_de_semana}')
