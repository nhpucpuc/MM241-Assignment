import gym_cutting_stock
import gymnasium as gym
from policy import GreedyPolicy, RandomPolicy
from student_submissions.s2213467.policy2213467 import Policy2213467
import pygame
pygame.display.set_mode((800,800))
# Create the environment
env = gym.make(
    "gym_cutting_stock/CuttingStock-v0",
    render_mode="human",  # Comment this line to disable rendering
)
NUM_EPISODES = 5

if __name__ == "__main__":
    # Reset the environment
    observation, info = env.reset(seed=42)

    # Test Policy 1
    policy = Policy2213467(policy_id=1)
    ep = 0
    while ep < NUM_EPISODES:
        action = policy.get_action(observation, info)
        observation, reward, terminated, truncated, info = env.step(action)

        if terminated or truncated:
            print(info)
            observation, info = env.reset(seed=ep)
            ep += 1

    # Reset the environment
    observation, info = env.reset(seed=42)

    # Test Policy 2
    policy = Policy2213467(policy_id=2)
    ep = 0
    while ep < NUM_EPISODES:
        action = policy.get_action(observation, info)
        observation, reward, terminated, truncated, info = env.step(action)

        if terminated or truncated:
            print(info)
            observation, info = env.reset(seed=ep)
            ep += 1

    # Uncomment the following code to test your policy
    # # Reset the environment
    # observation, info = env.reset(seed=42)
    # print(info)

    # policy2210xxx = Policy2210xxx(policy_id=1)
    # for _ in range(200):
    #     action = policy2210xxx.get_action(observation, info)
    #     observation, reward, terminated, truncated, info = env.step(action)
    #     print(info)

    #     if terminated or truncated:
    #         observation, info = env.reset()

env.close()