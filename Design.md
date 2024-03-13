# Chat Personality Design

### High Level Design

Create a chat bot framework which tries to reduce the number of tokens needed to send to ChatGPT, but capture some of the natural interactiviity of a standard chat bot interaction.

It does this by programatically defining some conversation flow states and tracking some state. It uses ChatGPT to generate responses for each of the given states. Caching the best ones for use later.

### Detailed brainstorm

Allow user to create a personality profile for the chat bot. Includes a list of personality traits, manerisms, physical props / descriptions, etc. These will be included in the generative prompts for the text chat.

Create a very simple "conversation flow" state machine, each state resulting in a response type. Some examples could be 'greeting', 'affirmative', 'negative', 'suggestion', 'request'.

For each of these states, it calls out to ChatGPT for a textual response. This includes in the prompt the personality / physical state above and asks for a response to fulfil the given conversation state.

These responses are cached for a given personality / state combination. The system will remember a number of responses for each situation (stored in a data text file), and return a random one from the list. User can up or downvote a response to request new ones from ChatGPT, hopefully slowly improving the responses.