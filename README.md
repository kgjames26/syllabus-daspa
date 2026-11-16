# Collection FLESco · DASPA — moteur des syllabus

Génère les PDF élève et enseignant des 3 volumes (HTML + Chrome headless → PDF).

## Reprendre le travail (pour Claude)
1. `python3 build/guide.py` — guide général (out/00_Guide_general_et_progression.pdf)
2. Chaque module = `build/mN.py` avec une fonction `build_mN(start, tstart, render)`.
   Modèle à copier : `build/v2_m5.py` (le plus récent) (utilisent les gabarits de `lib/module.py`).
3. `python3 build/vol1.py` — assemble modules + annexes + table des matières (calculée depuis les pages réelles, lib/toc.py ; pagination mesurée par Chrome, lib/measure.py) en
   `out/VOLUME_1_Premiers_pas_ELEVE.pdf` et `out/VOLUME_1_Premiers_pas_PROF.pdf`.
4. Progression complète des 3 volumes : `lib/progression.py`.

## État
- Volume 2 « Je me débrouille » (A2, 14 modules) : M1-M5 faits (build/v2_m*.py ; M5 = 45 p. élève + 16 p. livret, modèle le plus récent). Réglages V2 dans lib/v2.py (★ Coup de pouce remplace ★ Alpha, couverture). Assemblage : python3 build/vol2.py (élève 211 p., prof 71 p.). Suite : V2 M6 « Découvrir la Belgique ».
- lib/art.py : humeur « fache » ajoutée aux avatars (sourcils froncés).
- Volume 1 : TERMINÉ — 12 modules + annexes (8 p. de mémos, build/annexes.py) + table des matières détaillée et index (lib/toc.py), en tête du PDF prof et à la fin du PDF élève.
- Volumes 2 et 3 : à faire (créer build/vol2.py, vol3.py sur le modèle de vol1.py).
- Taille choisie pour la suite : modules complets (40-50 pages).

- Lien symbolique nécessaire : `ln -sfn <dépôt> /home/claude/syllabus` (chemins codés en dur).
## Outils
lib/base.py (CSS, Book, Ex, composants) · lib/art.py (personnages, pictos, visages) · lib/alpha.py (pages ★ Alpha) · lib/module.py (plan de travail, livret enseignant, gabarits) · lib/render.py (PDF).
