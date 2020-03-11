import random

# move to enemy
#   Distance to enemy           0 - 100 (int) 1
#   Gun is not loaded           -100    (bool) 1
# fire at enemy
#   Proximity to Enemy < 50     75      (int) 1
#   Cannot make it to cover     50      (bool) 1
#   Gun is not loaded           -125    (bool) 1
# move to cover
#   is not in cover             50      (bool) 1
#   prx to cover < 50           50      (int) 1
# load
#   gun not loaded              75      (bool) 1
#   is in cover                 50      (bool) 1
#   gun is loaded               -125    (bool) 1


can_cover = False;
cover = False;
loaded = True;
prox_to_enemy = 0;
prox_to_cover = 0;


def run():
    #randomize()
    while(1):
        print(choice());


def choice():
    random.seed()
    can_cover = random.choice([True, False])
    cover = random.choice([True, False])
    loaded = random.choice([True, False])
    prox_to_enemy = random.randint(0, 100)
    prox_to_cover = random.randint(0, 100)

    m_t_e = 0;
    f_a_e = 0;
    m_t_c = 0;
    l_ = 0;
    #move to nemey
    m_t_e += prox_to_enemy
    if (loaded):
        m_t_e += -100;

    #fire at enemy
    if (prox_to_enemy < 50):
        f_a_e += 75
    if (not can_cover):
        f_a_e += 50
    if (loaded):
        f_a_e += -125

    #Move to cover
    if (not cover):
        m_t_c += 50
    if (prox_to_cover < 50):
        m_t_c += 50

    #Load
    if (not loaded):
        l_ += 75
    if (cover):
        l_ += 50
    if (loaded):
        l_ += -125

    #print(m_t_e)
    #print(m_t_c)
    #print(f_a_e)
    #print(l_)

    if (m_t_e > max(f_a_e, m_t_c, l_)):
        return "Move to enemy!"
    if (f_a_e > max(m_t_e, m_t_c, l_)):
        return "Fire at enemy!"
    if (m_t_c > max(m_t_e, f_a_e, l_)):
        return "Move to cover!"
    if (l_ > max(m_t_c, f_a_e, m_t_e)):
        return "Load!"




run()
