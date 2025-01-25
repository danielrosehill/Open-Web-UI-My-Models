#  Open Web UI Assistant & Custom Model Library (Jan 2025)

25-Jan-25

## Purpose Statement

The purpose of this repository is to share configurations for custom models that can be imported into the (excellent!) Open Web UI front end for interacting with large language models via their APIs.

As an upstream source for the configurations, this repository has my public assistants repository as a sub module. 

## Assistants? Custom models? A word about nomenclature

As AI tools have evolved at such an incredible pace, we've seen some emerging standards for how to configure what have typically been provided as assistants on dedicated platforms (say, OpenAI Assistants API).

The emerging norm is that there isn't a hard need to ringfence these type of LLM tools from other ones. Rather by adding a system prompt and a RAG pipeline to a standard "off the shelf" LLM (accessed via its API), the same intended behavior can be achieved. 

## General purpose LLM mimics

Accessing large language models by APIs is typically quite a different experience from using them on their consumer platforms. The models that are accessed in this manner have no system prompt attached to them to modify and guide their response to the user.

In addition to creating custom models, I also create a few "LLM mimics" - These involve pairing large language models with their popular consumer platforms in order to try to achieve a somewhat comparable user experience while maintaining the utility of API access.

Rarely, providers have actually shared their system prompts. Consider the case of Anthropic which [releases this publicly](https://docs.anthropic.com/en/release-notes/system-prompts). But other providers have taken a much more guarded view, regarding them as trade secrets. 

In the former case (Anthropic) It should be possible to recreate Claude with good precision by simply Creating a model that uses the specific API and the relevant system prompt.

In cases where the system prompts are not publicly disclosed, however, users have to rely upon their imagination, creativity, and perhaps in some cases even reverse engineering to attempt to configure ones that provide replicas of sorts.

## Notes About The Config Texts (For Assistants)

Because writing system prompts can be a long process, I've switched to using voice dictation for this purpose over the past few months. I typically use Open AI Whisper to dictate my configuration prompts. While this generally works pretty well and saves a lot of time over writing out longer prompts, it's not a perfect process. 

For one, it probably tends towards encouraging writing longer configurations that are necessary, which will increase the token usage. Secondly, I don't always catch the typos. And even when I find capitalization, if I don't think that it's going to degrade the utility of the system prompts, sometimes I don't have time to fix them. So if you're thinking about using any of these, it's worth giving them a proofread and an edit before adding them to your own instance.

At the moment, I'm most focused on getting these useful configurations out the door and working on different platforms. Over time, however, I do iterate and improve upon the most useful ones. But a lot of the configurations are best understood as more experimentary to understand What kind of LLM assistants can be created and how best to write the system prompts.

I frequently create assistants which are backed by knowledge stores, but, for obvious reasons, I can't always share the context data. For example, I have one medication tracking assistant which has my daily medication list as its contextual knowledge. I might share these without the context data and try to rewrite them in a way that they might be adapted for another user. 


## Author

Daniel Rosehill  
(public at danielrosehill dot com)

## Licensing

This repository is licensed under CC-BY-4.0 (Attribution 4.0 International) 
[License](https://creativecommons.org/licenses/by/4.0/)

### Summary of the License
The Creative Commons Attribution 4.0 International (CC BY 4.0) license allows others to:
- **Share**: Copy and redistribute the material in any medium or format.
- **Adapt**: Remix, transform, and build upon the material for any purpose, even commercially.

The licensor cannot revoke these freedoms as long as you follow the license terms.

#### License Terms
- **Attribution**: You must give appropriate credit, provide a link to the license, and indicate if changes were made. You may do so in any reasonable manner, but not in any way that suggests the licensor endorses you or your use.
- **No additional restrictions**: You may not apply legal terms or technological measures that legally restrict others from doing anything the license permits.

For the full legal code, please visit the [Creative Commons website](https://creativecommons.org/licenses/by/4.0/legalcode).