from .base import GebetaEnv
from gym.envs.registration import register


register(
    id='Gebeta-v0',
    entry_point='envs:GebetaEnv',
    kwargs = dict()
)
