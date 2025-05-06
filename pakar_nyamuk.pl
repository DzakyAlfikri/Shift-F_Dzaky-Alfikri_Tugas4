% PENYAKIT AKIBAT GIGITAN NYAMUK

:- dynamic gejala_pos/1.
:- dynamic gejala_neg/1.

penyakit("Malaria").
penyakit("Dengue").
penyakit("Zika").
penyakit("Chikungunya").

% Gejala masing-masing penyakit
gejala(demam_tinggi, "Malaria").
gejala(menggigil, "Malaria").
gejala(nyeri_otot, "Malaria").
gejala(mual, "Malaria").

gejala(demam_tinggi, "Dengue").
gejala(sakit_kepala, "Dengue").
gejala(nyeri_sendi, "Dengue").
gejala(bintik_merah, "Dengue").

gejala(demam_ringan, "Zika").
gejala(ruam, "Zika").
gejala(nyeri_sendi, "Zika").
gejala(irritasi_mata, "Zika").

gejala(demam_tinggi, "Chikungunya").
gejala(nyeri_sendi, "Chikungunya").
gejala(sakit_kepala, "Chikungunya").
gejala(lelah, "Chikungunya").

% Pertanyaan untuk masing-masing gejala
pertanyaan(demam_tinggi, "Apakah Anda mengalami demam tinggi?").
pertanyaan(menggigil, "Apakah Anda mengalami menggigil?").
pertanyaan(nyeri_otot, "Apakah Anda mengalami nyeri otot?").
pertanyaan(mual, "Apakah Anda merasa mual?").
pertanyaan(sakit_kepala, "Apakah Anda sakit kepala?").
pertanyaan(nyeri_sendi, "Apakah Anda mengalami nyeri sendi?").
pertanyaan(bintik_merah, "Apakah Anda memiliki bintik merah di kulit?").
pertanyaan(demam_ringan, "Apakah Anda mengalami demam ringan?").
pertanyaan(ruam, "Apakah Anda mengalami ruam kulit?").
pertanyaan(irritasi_mata, "Apakah Anda mengalami iritasi mata?").
pertanyaan(lelah, "Apakah Anda merasa lelah?").