import shugyo
env = shugyo.make('Shugyoに対応したUnityのGame')      # 環境を作る
env.configure(host="localhost", port="12345")       # なんかオプションがあれば

for _episode in range(10000):
    observation_n = env.reset()                     # 環境をリセットする
    for _times in range(2000):
        action_n = [[('KeyEvent', 'ArrowUp', True)] for ob in observation_n]
            # エージェントを記載する
        observation_n, reward_n, done_n, info = env.step(action_n)
            # Actionを実行して環境を1ステップすすめる
        env.render()
            #描画する
        if done_n:
            break
