alt = float(input('Digite a altura da parede: '))
lar = float(input('Digite a largura da parede: '))

area = alt * lar
tinta = area / 2

print('A parede de {:.0f}x{:.0f} tem {}m² de área e vai precisar de {} litros de tinta.'.format(alt, lar, area, tinta))