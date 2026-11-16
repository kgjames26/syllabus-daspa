# Collection FLESco · DASPA — moteur des syllabus

Génère les PDF élève et enseignant des 3 volumes (HTML + Chrome headless → PDF).

## Reprendre le travail (pour Claude)
1. `python3 build/guide.py` — guide général (out/00_Guide_general_et_progression.pdf)
2. Chaque module = `build/mN.py` avec une fonction `build_mN(start, tstart, render)`.
   Modèle à copier : `build/v2_m13.py` (le plus récent) (utilisent les gabarits de `lib/module.py`).
3. `python3 build/vol1.py` — assemble modules + annexes + table des matières (calculée depuis les pages réelles, lib/toc.py ; pagination mesurée par Chrome, lib/measure.py) en
   `out/VOLUME_1_Premiers_pas_ELEVE.pdf` et `out/VOLUME_1_Premiers_pas_PROF.pdf`.
4. Progression complète des 3 volumes : `lib/progression.py`.

## État
- Volume 2 « Je me débrouille » (A2, 14 modules) : M1-M13 faits (build/v2_m*.py ; M13 « Contes du monde » = 43 p. élève + 17 p. livret, modèle le plus récent (conte original « Le tambour de la pluie », 4e de couverture, légende de Bayard, schéma narratif en 5 cartes colorées) ; M12 « Démarches » : fonctions champ() et boxes() pour dessiner des formulaires administratifs (cases, cadres), courrier officiel annoté ①-⑨, clé QCM variée par rotation des options (qrot) ; M11 « Métiers et stages » ; M10 — fonction bars() de diagramme en barres SVG ; M9 : fonction label() d'étiquette nutritionnelle ; carte SVG de Belgique : fonction carte() dans build/v2_m6.py). Réglages V2 dans lib/v2.py (★ Coup de pouce remplace ★ Alpha, couverture). Assemblage : python3 build/vol2.py (élève 563 p., prof 211 p.). Suite : V2 M14 « Mes projets » (dernier module du volume 2).
- Volume 3 « Je réussis à l'école » (B1 + FLSco, 16 modules) : **M1 « Apprendre à apprendre » fait** (build/v3_m1.py = modèle V3 : couverture + « Mon livre » + sommaire, pages 🎓 Vers les épreuves CE1D / DELF B1, étiquettes de disciplines ; 49 p. élève + 17 p. livret). Réglages V3 dans lib/v3.py (CP, EPR, disc_tag, v3_cover, v3_mon_livre). Assemblage : python3 build/vol3.py (élève 53 p., prof 22 p.). Suite V3 : M2 « La langue des maths » — à prendre seulement après le V2 M14 (ordre de la collection).
- lib/art.py : humeur « fache » ajoutée aux avatars (sourcils froncés).
- Volume 1 : TERMINÉ — 12 modules + annexes (8 p. de mémos, build/annexes.py) + table des matières détaillée et index (lib/toc.py), en tête du PDF prof et à la fin du PDF élève.
- Volumes 2 et 3 : à faire (créer build/vol2.py, vol3.py sur le modèle de vol1.py).
- Taille choisie pour la suite : modules complets (40-50 pages).

- Lien symbolique nécessaire : `ln -sfn <dépôt> /home/claude/syllabus` (chemins codés en dur).
## Outils
lib/base.py (CSS, Book, Ex, composants) · lib/art.py (personnages, pictos, visages) · lib/alpha.py (pages ★ Alpha) · lib/module.py (plan de travail, livret enseignant, gabarits) · lib/render.py (PDF).
