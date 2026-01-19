import asyncio
from droidrun import DroidAgent, DroidrunConfig

async def main():
    config = DroidrunConfig()

    agent = DroidAgent(
        goal="""
        Activate Study Mode for the topic Electromagnetism.

        Open the YouTube app and search for "Electromagnetism tutorial".
        Shortlist and analyze at least 5 videos based on educational relevance.
        Select and open the best educational video.

        Open ChatGPT and explain the concepts covered in the selected video.
        Save the video link and explanation as study notes in Notepad.
        """,
        config=config
    )

    result = await agent.run()
    print("Success:", result.success)

if __name__ == "__main__":
    asyncio.run(main())
