# два человека идут навстречу с известной скоростью, начальное расстояние между ними дано,
# это время между ними бегает собака с заданной скоростью, добегая до одного, разворачивается
# и бежит к другому, пока люди не сблизятся. Найти сколько раз собака пробежит от человека к человеку.
sp_fr1 = 4
sp_fr2 = 5
sp_dog = 10
distance = 1000
distance_lim = 10
dog_count = 0
dog_direction = 1
while distance > distance_lim:
    speed = 0
    if dog_direction == 1:
        speed = sp_fr1 + sp_dog
        dog_direction = 2
    else:
        speed = sp_fr2 + sp_dog
        dog_direction = 1
    if distance < 1:
        break
    time_to = distance / speed
    distance = distance - time_to * (sp_fr1 + sp_fr2)
    dog_count += 1
    # print(distance) # дистанция между людьми после каждого цикла
print(f'собака сделает {dog_count} "рейсов"')
