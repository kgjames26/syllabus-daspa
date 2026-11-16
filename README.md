# Collection FLESco · DASPA — moteur des syllabus

Génère les PDF élève et enseignant des 3 volumes (HTML + Chrome headless → PDF).

## Reprendre le travail (pour Claude)
1. `python3 build/guide.py` — guide général (out/00_Guide_general_et_progression.pdf)
2. Chaque module = `build/mN.py` avec une fonction `build_mN(start, tstart, render)`.
   Modèle à copier : `build/v2_m7.py` (le plus récent) (utilisent les gabarits de `lib/module.py`).
3. `python3 build/vol1.py` — assemble modules + annexes + table des matières (calculée depuis les pages réelles, lib/toc.py ; pagination mesurée par Chrome, lib/measure.py) en
   `out/VOLUME_1_Premiers_pas_ELEVE.pdf` et `out/VOLUME_1_Premiers_pas_PROF.pdf`.
4. Progression complète des 3 volumes : `lib/progression.py`.

## État
- Volume 2 « Je me débrouille » (A2, 14 modules) : M1-M7 faits (build/v2_m*.py ; M7 = 44 p. élève + 15 p. livret, modèle le plus récent ; carte SVG de Belgique réutilisable : fonction carte() dans build/v2_m6.py, importée par v2_m7). Réglages V2 dans lib/v2.py (★ Coup de pouce remplace ★ Alpha, couverture). Assemblage : python3 build/vol2.py (élève 300 p., prof 104 p.). Suite : V2 M8 « Écrans et médias ».
- Volume 3 « Je réussis à l'école » (B1 + FLSco, 16 modules) : **M1 « Apprendre à apprendre » fait** (build/v3_m1.py = modèle V3 : couverture + « Mon livre » + sommaire, pages 🎓 Vers les épreuves CE1D / DELF B1, étiquettes de disciplines ; 49 p. élève + 17 p. livret). Réglages V3 dans lib/v3.py (CP, EPR, disc_tag, v3_cover, v3_mon_livre). Assemblage : python3 build/vol3.py (élève 53 p., prof 22 p.). Suite V3 : M2 « La langue des maths » — à prendre seulement après le V2 M14 (ordre de la collection).
- lib/art.py : humeur « fache » ajoutée aux avatars (sourcils froncés).
- Volume 1 : TERMINÉ — 12 modules + annexes (8 p. de mémos, build/annexes.py) + table des matières détaillée et index (lib/toc.py), en tête du PDF prof et à la fin du PDF élève.
- Volumes 2 et 3 : à faire (créer build/vol2.py, vol3.py sur le modèle de vol1.py).
- Taille choisie pour la suite : modules complets (40-50 pages).

- Lien symbolique nécessaire : `ln -sfn <dépôt> /home/claude/syllabus` (chemins codés en dur).
## Outils
lib/base.py (CSS, Book, Ex, composants) · lib/art.py (personnages, pictos, visages) · lib/alpha.py (pages ★ Alpha) · lib/module.py (plan de travail, livret enseignant, gabarits) · lib/render.py (PDF).
