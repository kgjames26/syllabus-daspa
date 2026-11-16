# Collection FLESco · DASPA — moteur des syllabus

Génère les PDF élève et enseignant des 3 volumes (HTML + Chrome headless → PDF).

## Reprendre le travail (pour Claude)
1. `python3 build/guide.py` — guide général (out/00_Guide_general_et_progression.pdf)
2. Chaque module = `build/mN.py` avec une fonction `build_mN(start, tstart, render)`.
   Modèle à copier : `build/v2_m14.py` (le plus récent en V2) ou `build/v3_m3.py` (V3, le plus récent) (utilisent les gabarits de `lib/module.py`).
3. `python3 build/vol1.py` — assemble modules + annexes + table des matières (calculée depuis les pages réelles, lib/toc.py ; pagination mesurée par Chrome, lib/measure.py) en
   `out/VOLUME_1_Premiers_pas_ELEVE.pdf` et `out/VOLUME_1_Premiers_pas_PROF.pdf`.
4. Progression complète des 3 volumes : `lib/progression.py`.

## État
- Volume 2 « Je me débrouille » (A2, 14 modules) : **TERMINÉ** — M1-M14 faits (build/v2_m*.py). M14 « Mes projets » = 45 p. élève + 18 p. livret (futur simple, souhaits, organigramme des études FWB en HTML : fonction organigramme() dans build/v2_m14.py, lettre formelle annotée ①-⑧, brochure d'école, révision spiralée de tout le volume, page « Bilan du volume 2 ») ; M13 « Contes du monde » ; M12 « Démarches » : fonctions champ() et boxes() (formulaires), clé QCM variée par rotation des options (qrot) ; M10 — bars() ; M9 — label() ; carte SVG de Belgique : carte() dans build/v2_m6.py. Réglages V2 dans lib/v2.py. Assemblage : python3 build/vol2.py (élève 609 p., prof 230 p.).
- Volume 3 « Je réussis à l'école » (B1 + FLSco, 16 modules) : M1-M3 faits. M1 « Apprendre à apprendre » (build/v3_m1.py : couverture + « Mon livre » + sommaire, pages 🎓 Vers les épreuves CE1D / DELF B1, étiquettes de disciplines ; 49 p. élève + 17 p. livret). M2 « La langue des maths » (build/v3_m2.py : 44 p. élève + 17 p. livret ; fonctions enonce() pour les énoncés étiquetés MATHS et figures() pour les figures géométriques en SVG ; facture belge HTVA/TVA/TVAC ; problèmes de type CE1D). M3 « La langue des sciences » (build/v3_m3.py, modèle V3 le plus récent : 44 p. élève + 17 p. livret ; SVG réutilisables plante() (schéma légendé ou à légender), montage() (montage de chauffage), courbe() (graphique en ligne) ; étiquette de produit avec pictogrammes CLP ; rapport d'expérience en 6 parties). Réglages V3 dans lib/v3.py (CP, EPR, disc_tag, v3_cover, v3_mon_livre). Assemblage : python3 build/vol3.py (élève 144 p., prof 59 p.). **Prochain module : V3 M4 « Raconter l'Histoire »** (modèle : build/v3_m3.py).
- Contrôle de mise en page : les pages ont overflow:hidden ; vérifier qu'aucun bloc ne descend sous le pied de page (`python3 lib/overflow.py out/V?_M?_eleve.html`) et que les numéros d'exercices se suivent (créer les exercices dans l'ordre d'affichage). Si le plan de travail déborde (> 100 exercices), compacter ses cases après plan_de_travail() (voir la fin de build/v3_m2.py). Si les scripts du livret débordent de peu sur une 2e page presque vide, raccourcir quelques scripts (coût estimé par lib/module.py:_cost, budget 190).
- lib/art.py : humeur « fache » ajoutée aux avatars (sourcils froncés).
- Volume 1 : TERMINÉ — 12 modules + annexes (8 p. de mémos, build/annexes.py) + table des matières détaillée et index (lib/toc.py), en tête du PDF prof et à la fin du PDF élève.
- Taille choisie pour la suite : modules complets (40-50 pages).

- Lien symbolique nécessaire : `ln -sfn <dépôt> /home/claude/syllabus` (chemins codés en dur).
## Outils
lib/base.py (CSS, Book, Ex, composants) · lib/art.py (personnages, pictos, visages) · lib/alpha.py (pages ★ Alpha) · lib/module.py (plan de travail, livret enseignant, gabarits) · lib/render.py (PDF).
