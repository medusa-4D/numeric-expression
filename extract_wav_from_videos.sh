videos=$(ls data/videos/*.mp4)
for vid in ${videos}; do
    bname=$(basename ${vid})
    ffmpeg -i $vid -ac 1 -f wav data/wavs/${bname/.mp4/.wav}
done