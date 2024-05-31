import game
import jugador

p1 = jugador.Player(1, 'a')
p2 = jugador.Player(2, 'b')
g1= game.Game(p1, p2, 3)

print(p1)
print(p2)

game.Game.play(g1)

g1.winner().toString()#No consigo mostrar el ganador, no entiendo porque.