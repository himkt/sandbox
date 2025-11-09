import os

import dspy


def main():
    lm = dspy.LM(
        'openrouter/openai/gpt-4.1',
        api_key=os.environ["OPENROUTER_API_KEY"],
        cache=False,
    )
    dspy.configure(lm=lm)

    # Example from the XSum dataset.
    document = """The 21-year-old made seven appearances for the Hammers and netted his only goal for them in a Europa League qualification round match against Andorran side FC Lustrains last season. Lee had two loan spells in League One last term, with Blackpool and then Colchester United. He scored twice for the U's but was unable to save them from relegation. The length of Lee's contract with the promoted Tykes has not been revealed. Find all the latest football transfers on our dedicated page."""
    summarize = dspy.ChainOfThought('document -> summary: str')
    response = summarize(document=document)
    print(response.summary)

    summarize = dspy.Predict('document -> summary: str')
    response = summarize(document=document)
    print(response.summary)


if __name__ == "__main__":
    main()
