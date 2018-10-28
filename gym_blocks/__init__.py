from gym.envs.registration import register

register(
    id='BlocksFam-v0',
    entry_point='gym_blocks.envs:BlocksFamEnv'
)

register(
    id='BlocksObs-v0',
    entry_point='gym_blocks.envs:BlocksObsEnv'
)

register(
    id='BlocksTest-v0',
    entry_point='gym_blocks.envs:BlocksTestEnv'
)
