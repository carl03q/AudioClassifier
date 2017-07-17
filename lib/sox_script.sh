a=0;
echo $1
echo $2
for file in $1*.mp3; do
   a=$((a+1));
   out_name=$2$a.png
   #echo $out_name
   sox "$file" -n spectrogram -Y 130 -l -r -m -o $out_name;
done
