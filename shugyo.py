
class shugyo():
    def __init__(self, game):
        self.game = game

    def configure(self, host='localhost', port=3326):
        print('configure')

    def reset(self):
        print('reset')
        observation = [1,2,3]
        return observation

    def step(self, action):
        print('step')
        observation = [1,2,3]
        reward = 0
        done = True
        info = 'hogehoge'
        return observation, reward, done, info

    def render(self):
        print('render')


def make(game):
    print("this is make")
    return shugyo(game)
