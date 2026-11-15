# Collection FLESco · DASPA — moteur des syllabus

Génère les PDF élève et enseignant des 3 volumes (HTML + Chrome headless → PDF).

## Reprendre le travail (pour Claude)
1. `python3 build/guide.py` — guide général (out/00_Guide_general_et_progression.pdf)
2. Chaque module = `build/mN.py` avec une fonction `build_mN(start, tstart, render)`.
   Modèle à copier : `build/m8.py` (le plus récent) (utilisent les gabarits de `lib/module.py`).
3. `python3 build/vol1.py` — assemble tous les modules trouvés en
   `out/VOLUME_1_Premiers_pas_ELEVE.pdf` et `out/VOLUME_1_Premiers_pas_PROF.pdf`.
4. Progression complète des 3 volumes : `lib/progression.py`.

## État
- Volume 1 : modules 1 à 8 faits (M8 = 37 p. élève + 11 p. prof). À faire : M9 Ma ville, M10 Ma journée, M11 Loisirs, M12 Hier et demain + annexes.
- Volumes 2 et 3 : à faire (créer build/vol2.py, vol3.py sur le modèle de vol1.py).
- Taille choisie pour la suite : modules complets (40-50 pages).

- Lien symbolique nécessaire : `ln -sfn <dépôt> /home/claude/syllabus` (chemins codés en dur).
## Outils
lib/base.py (CSS, Book, Ex, composants) · lib/art.py (personnages, pictos, visages) · lib/alpha.py (pages ★ Alpha) · lib/module.py (plan de travail, livret enseignant, gabarits) · lib/render.py (PDF).
