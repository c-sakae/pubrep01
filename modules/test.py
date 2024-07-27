from audiocraft.models import musicgen
from audiocraft.data.audio import audio_write
emo_path = './emo.txt' #str
out_dur = 6.0 #sec
out_name = 'a'

model = musicgen.MusicGen.get_pretrained('facebook/musicgen-small')
model.set_generation_params(
    duration = out_dur
)

with open(emo_path) as f:
    str = f.read()

output = model.generate(
    descriptions = [
        str
    ],
    progress = True
)

audio_write(f'../sounds/{out_name}',
            output[0].cpu(), model.sample_rate)
