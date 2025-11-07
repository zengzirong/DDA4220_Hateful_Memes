from huggingface_hub import snapshot_download

# Download the entire dataset repository (including img/)
snapshot_download(repo_id="neuralcatcher/hateful_memes", repo_type="dataset", local_dir="tmp_data")