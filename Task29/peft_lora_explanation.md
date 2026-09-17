# PEFT / LoRA — short explanation

**Quantization** shrinks an already-trained model so it runs with less RAM and lower latency (e.g. `q4_K_M` tags in Ollama). **LoRA** and **PEFT** shrink the *cost of adapting* a model: instead of updating every weight, you train a tiny add-on.

In a `LoraConfig`, **`r` (rank)** is the size of the low-rank update matrices LoRA injects next to frozen layers. A very small `r` means fewer trainable parameters (cheaper, less capacity to change behavior); a very large `r` approaches the flexibility of a fuller update but costs more compute and memory — so you pick a middle ground that fits your budget.

**`target_modules`** names which layers get those adapters (commonly attention projections like `q_proj` and `v_proj`). Only those modules receive LoRA matrices; everything else stays frozen. That is why LoRA is dramatically cheaper than a full fine-tune: you train a tiny fraction of the parameters instead of billions of base weights.

**PEFT** is both the family of techniques (LoRA, prefix tuning, adapters, …) and Hugging Face’s library that implements them (`LoraConfig`, `get_peft_model`). Quantization makes *serving* cheap; LoRA/PEFT make *customizing* cheap — together they are how you adapt and run modern LLMs without a huge GPU cluster.
