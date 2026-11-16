"""Volume 1 · Annexes : mémos à consulter toute l'année (élève)."""
import sys
sys.path.insert(0, '/home/claude/syllabus')
from lib.base import *
from lib.art import *

AC = "#455A64"


def conj(title, forms, note=""):
    return (f'<div class="card" style="background:#fff;padding:2.5mm"><b style="color:{AC}">{title}</b><p class="sm" style="margin:1mm 0;line-height:1.55">' + "<br>".join(forms) + '</p>' +
            (f'<div class="xs muted">{note}</div>' if note else '') + '</div>')


P6 = ["je", "tu", "il / elle / on", "nous", "vous", "ils / elles"]


def c6(title, ends, note="", elide=False):
    pr = P6[:]
    if elide:
        pr[0] = "j'"
    return conj(title, [f'{p}{"" if p.endswith(chr(39)) else " "}<b>{e}</b>' for p, e in zip(pr, ends)], note)


def build_annexes(start=1, render=False):
    b = Book("V1 · Mémos", "Volume 1 · Premiers pas · Annexes · Mes mémos", AC, start=start)
    head = lambda t, sub: f'<div style="background:{AC};color:#fff;margin:-17mm -14mm 5mm -14mm;padding:14mm 14mm 4mm 14mm"><div style="font-size:11pt;font-weight:700;opacity:.85">📎 ANNEXE · MES MÉMOS</div><div style="font-size:24pt;font-weight:800">{t}</div><div class="sm" style="opacity:.9">{sub}</div></div>'

    # 1. Conjugaison : présent
    b.page(head("Conjuguer au présent (1)", "Les verbes les plus utiles. Module où on les apprend entre parenthèses.") + '<div class="grid3">' +
           c6("ÊTRE (M1, M4)", ["suis", "es", "est", "sommes", "êtes", "sont"]) + c6("AVOIR (M1, M4)", ["ai", "as", "a", "avons", "avez", "ont"], elide=True) + c6("ALLER (M9)", ["vais", "vas", "va", "allons", "allez", "vont"]) +
           c6("FAIRE (M11)", ["fais", "fais", "fait", "faisons", "faites", "font"]) + c6("PARLER · verbes en -er (M3)", ["parle", "parles", "parle", "parlons", "parlez", "parlent"], "Les terminaisons : -e, -es, -e, -ons, -ez, -ent (muet !)") +
           c6("PRENDRE (M9)", ["prends", "prends", "prend", "prenons", "prenez", "prennent"]) + '</div>' +
           '<div class="astuce mt4">Avec <b>on</b>, le verbe est comme avec <b>il / elle</b> : on parle, on va, on fait. · Devant une voyelle : je → <b>j\'</b> (j\'ai, j\'aime, j\'habite).</div>', "Mémo conjugaison", levels=False)
    b.page(head("Conjuguer au présent (2)", "Verbes irréguliers et verbes pronominaux.") + '<div class="grid3">' +
           c6("METTRE (M8)", ["mets", "mets", "met", "mettons", "mettez", "mettent"]) + c6("VOULOIR (M7)", ["veux", "veux", "veut", "voulons", "voulez", "veulent"], "Poli : je voudrais") + c6("POUVOIR (M7)", ["peux", "peux", "peut", "pouvons", "pouvez", "peuvent"]) +
           c6("DEVOIR (M11)", ["dois", "dois", "doit", "devons", "devez", "doivent"]) + c6("VENIR", ["viens", "viens", "vient", "venons", "venez", "viennent"], "Je viens de… (M1)") +
           conj("SE LEVER · pronominal (M10)", ["je <b>me</b> lève", "tu <b>te</b> lèves", "il / elle <b>se</b> lève", "nous <b>nous</b> levons", "vous <b>vous</b> levez", "ils / elles <b>se</b> lèvent"], "me, te, se → m', t', s' devant une voyelle") + '</div>' +
           '<h3 class="mt4">L\'impératif : donner une consigne, un conseil (M5, M9)</h3>' + table(["Verbe", "tu", "nous", "vous"], [["écouter", "Écoute !", "Écoutons !", "Écoutez !"], ["aller", "Va !", "Allons !", "Allez !"], ["prendre", "Prends !", "Prenons !", "Prenez !"], ["mettre", "Mets !", "Mettons !", "Mettez !"], ["se lever", "Lève-toi !", "Levons-nous !", "Levez-vous !"]], ["40mm", "47mm", "47mm", "48mm"]),
           "Mémo conjugaison", levels=False)
    pp = [("manger", "mangé"), ("jouer", "joué"), ("parler", "parlé"), ("faire", "fait"), ("prendre", "pris"), ("mettre", "mis"), ("voir", "vu"), ("lire", "lu"), ("boire", "bu"), ("avoir", "eu"), ("être", "été"), ("écrire", "écrit"), ("dormir", "dormi"), ("finir", "fini"), ("vouloir", "voulu"), ("pouvoir", "pu")]
    b.page(head("Parler du passé et du futur", "Le passé composé et le futur proche (module 12).") +
           '<div class="grid2"><div class="card" style="background:#E8EAF6"><b>⬅️ PASSÉ COMPOSÉ</b> = avoir + participe passé<p class="big">Hier, j\'<b>ai mangé</b>.</p><p class="sm">j\'ai · tu as · il a · nous avons · vous avez · ils ont + mangé<br>Négation : je <b>n\'</b>ai <b>pas</b> mangé.<br>⚠️ avec être : je <b>suis allé(e)</b> (volume 2)</p></div>' +
           '<div class="card" style="background:#E3F2E1"><b>➡️ FUTUR PROCHE</b> = aller + infinitif<p class="big">Demain, je <b>vais manger</b>.</p><p class="sm">je vais · tu vas · il va · nous allons · vous allez · ils vont + manger<br>Négation : je <b>ne</b> vais <b>pas</b> manger.</p></div></div>' +
           '<h3 class="mt4">Les participes passés à connaître</h3><div class="grid4">' + "".join(f'<div class="card c" style="padding:1.5mm"><span class="sm">{a}</span> → <b>{p}</b></div>' for a, p in pp) + '</div>' +
           '<h3 class="mt4">Les mots du temps</h3><p>⬅️ hier · avant-hier · la semaine dernière · le week-end dernier · il y a 2 jours &nbsp;|&nbsp; 📍 aujourd\'hui · maintenant &nbsp;|&nbsp; ➡️ demain · ce soir · la semaine prochaine · l\'année prochaine</p>', "Mémo conjugaison", levels=False)

    # 2. Grammaire
    b.page(head("Les petits mots de la grammaire", "Articles, possessifs, négation, accords, prépositions.") +
           table(["", "masculin", "féminin", "devant voyelle", "pluriel", "Module"], [["un / une", "<b>un</b> livre", "<b>une</b> table", "un ami / une amie", "<b>des</b> livres", "M2"], ["le / la", "<b>le</b> livre", "<b>la</b> table", "<b>l\'</b>école", "<b>les</b> livres", "M2"],
                 ["du / de la", "<b>du</b> pain", "<b>de la</b> soupe", "<b>de l\'</b>eau", "<b>des</b> frites", "M6"], ["mon / ma", "<b>mon</b> père", "<b>ma</b> mère", "<b>mon</b> amie", "<b>mes</b> parents", "M4"], ["ton / ta", "<b>ton</b> sac", "<b>ta</b> sœur", "<b>ton</b> école", "<b>tes</b> amis", "M4"], ["son / sa", "<b>son</b> frère", "<b>sa</b> tante", "<b>son</b> histoire", "<b>ses</b> cousins", "M4"],
                 ["à + …", "<b>au</b> parc", "<b>à la</b> gare", "<b>à l\'</b>école", "<b>aux</b> toilettes", "M9"], ["de + …", "en face <b>du</b> parc", "<b>de la</b> poste", "<b>de l\'</b>école", "<b>des</b> magasins", "M9"]], ["24mm", "32mm", "32mm", "36mm", "34mm", "16mm"]) +
           '<div class="grid2 mt4"><div class="card" style="background:#fff"><b>🚫 La négation (M6, M10, M12)</b><p class="sm">Je <b>ne</b> mange <b>pas</b>. · Je <b>n\'</b>aime <b>pas</b>.<br>Je <b>ne</b> bois <b>jamais</b> de café.<br>J\'ai <b>un</b> chat → Je n\'ai <b>pas de</b> chat.<br>Je <b>ne</b> me lève <b>pas</b>. · Je <b>n\'</b>ai <b>pas</b> mangé.</p></div>' +
           '<div class="card" style="background:#fff"><b>🎨 L\'accord de l\'adjectif (M4, M8)</b><p class="sm">un pull vert · une robe vert<b>e</b> · des pulls vert<b>s</b> · des robes vert<b>es</b><br>⚠️ blanc → blanche · violet → violette · gentil → gentille<br>déjà un e : rouge, jaune, rose · jamais d\'accord : orange, marron</p></div></div>' +
           '<div class="grid2 mt2"><div class="card" style="background:#fff"><b>📍 Où ? (M2, M9)</b><p class="sm">sur · sous · dans · devant · derrière · à côté de · en face de · entre · près de · loin de · au coin de</p></div><div class="card" style="background:#fff"><b>🚌 Comment ? (M9)</b><p class="sm"><b>à</b> pied · <b>à</b> vélo · <b>en</b> bus · <b>en</b> voiture · <b>en</b> train · <b>en</b> tram · <b>en</b> métro</p></div></div>', "Mémo grammaire", levels=False)
    qs = [("Qui ?", "une personne", "Qui est-ce ?"), ("Qu'est-ce que ?", "une chose", "Qu'est-ce que tu fais ?"), ("Où ?", "un lieu", "Où est la gare ?"), ("Quand ?", "un moment", "Quand est le match ?"), ("À quelle heure ?", "une heure", "À quelle heure tu viens ?"),
          ("Comment ?", "la manière", "Comment tu t'appelles ?"), ("Combien ?", "un nombre, un prix", "Combien ça coûte ?"), ("Pourquoi ?", "une raison", "Pourquoi tu es triste ? — Parce que…"), ("Quel / quelle ?", "un choix", "Quel âge as-tu ? Quelle heure est-il ?"), ("Est-ce que ?", "oui / non", "Est-ce que tu viens ?")]
    b.page(head("Poser des questions · les phrases utiles", "Pour parler en classe et dans la vie.") +
           table(["Le mot", "pour demander…", "Exemple"], [[f"<b>{a}</b>", f'<span class="sm">{b2}</span>', c] for a, b2, c in qs], ["40mm", "42mm", "100mm"]) +
           '<h3 class="mt4">🙋 Les phrases de la classe</h3><div class="grid2">' + "".join(f'<div class="card" style="padding:2mm"><span class="sm">{t}</span></div>' for t in [
               "Je ne comprends pas.", "Vous pouvez répéter, s'il vous plaît ?", "Comment on dit … en français ?", "Qu'est-ce que ça veut dire ?", "Comment ça s'écrit ?", "Je peux aller aux toilettes ?",
               "J'ai fini. Qu'est-ce que je fais maintenant ?", "Je peux travailler avec … ?", "Pardon, je suis en retard.", "Vous pouvez m'aider, s'il vous plaît ?", "Je n'ai pas de stylo. Tu peux me prêter … ?", "Merci ! · De rien. · Bonne journée !"]) + '</div>',
           "Mémo grammaire", levels=False)

    # 3. Sons et lettres
    sons = [("[a]", "a, à", "🍍 ananas"), ("[i]", "i, î, y", "🏝️ île"), ("[o]", "o, au, eau", "🚗 auto"), ("[ɔ]", "o", "🦴 os"), ("[u]", "ou", "🐺 loup"), ("[y]", "u", "🌙 lune"), ("[e]", "é, er, ez, et", "☀️ été"), ("[ɛ]", "è, ê, ai, ei, e+2 cons.", "👩 mère"),
            ("[ə]", "e", "🍰 le gâteau"), ("[ø]", "eu (fin)", "🔵 bleu"), ("[œ]", "eu + cons.", "🌸 fleur"), ("[ɑ̃]", "an, am, en, em", "👩 maman"), ("[ɛ̃]", "in, im, ain, ein, un", "🍞 pain"), ("[ɔ̃]", "on, om", "🍬 bonbon"), ("[wa]", "oi", "👑 roi"), ("[wɛ̃]", "oin", "🔭 loin"),
            ("[ʃ]", "ch", "🐈 chat"), ("[ʒ]", "j, g (e, i)", "🦒 girafe"), ("[k]", "c, k, qu", "☕ café"), ("[g]", "g, gu", "🍰 gâteau"), ("[s]", "s, ss, c (e, i), ç", "🐍 serpent"), ("[z]", "z, s entre 2 voyelles", "🦓 zèbre"), ("[ɲ]", "gn", "⛰️ montagne"), ("[j]", "ill, y, i + voyelle", "👧 fille")]
    b.page(head("Les sons et les lettres", "Un son peut s'écrire de plusieurs façons. Je regarde le mot-repère.") +
           table(["Son", "Je l'écris…", "Mot-repère", "Son", "Je l'écris…", "Mot-repère"], [[f'<b>{a[0]}</b>', a[1], a[2], f'<b>{c[0]}</b>', c[1], c[2]] for a, c in zip(sons[:12], sons[12:])], ["14mm", "40mm", "36mm", "14mm", "42mm", "36mm"]) +
           '<div class="grid2 mt4"><div class="card" style="background:#fff"><b>🔤 L\'alphabet</b><p style="font-size:13pt;letter-spacing:.5mm">A B C D E F G H I J K L M N O P Q R S T U V W X Y Z</p><p class="sm">a b c d e f g h i j k l m n o p q r s t u v w x y z</p><p class="xs muted">Voyelles : a e i o u y · les autres = consonnes</p></div>' +
           '<div class="card" style="background:#fff"><b>🤫 Les lettres muettes (M10)</b><p class="sm">Souvent à la fin : peti<span style="color:#bbb">t</span>, gran<span style="color:#bbb">d</span>, troi<span style="color:#bbb">s</span>, deu<span style="color:#bbb">x</span>, ils parl<span style="color:#bbb">ent</span>.<br>Le <b>h</b> ne se dit jamais : l\'<span style="color:#bbb">h</span>ôpital.<br><b>c</b> + a, o, u = [k] (café) · <b>c</b> + e, i = [s] (cinéma) · <b>ç</b> = [s] (garçon)</p></div></div>',
           "Mémo sons", levels=False)

    # 4. Nombres, heure, date, argent
    n0 = ["zéro", "un", "deux", "trois", "quatre", "cinq", "six", "sept", "huit", "neuf", "dix", "onze", "douze", "treize", "quatorze", "quinze", "seize", "dix-sept", "dix-huit", "dix-neuf", "vingt"]
    diz = [("20", "vingt"), ("30", "trente"), ("40", "quarante"), ("50", "cinquante"), ("60", "soixante"), ("70", "septante 🇧🇪"), ("80", "quatre-vingts"), ("90", "nonante 🇧🇪"), ("100", "cent"), ("1000", "mille")]
    b.page(head("Les nombres · l'heure · la date · l'argent", "Modules 1, 3 et 7.") +
           '<div class="grid2"><div class="card" style="background:#fff"><b>0 → 20</b><div class="grid3 sm" style="gap:.5mm">' + "".join(f'<span><b>{i}</b> {w}</span>' for i, w in enumerate(n0)) + '</div></div>' +
           '<div class="card" style="background:#fff"><b>Les dizaines</b><div class="grid2 sm" style="gap:.5mm">' + "".join(f'<span><b>{n}</b> {w}</span>' for n, w in diz) + '</div><p class="xs muted">21 vingt et un · 22 vingt-deux · 71 septante et un · 81 quatre-vingt-un · 200 deux cents · 250 deux cent cinquante</p></div></div>' +
           '<div class="grid3 mt2"><div class="card" style="background:#fff"><b>🕐 L\'heure (M3, M10)</b><p class="sm">Quelle heure est-il ? Il est…<br>8 h · huit heures<br>8 h 15 · huit heures et quart<br>8 h 30 · huit heures et demie<br>8 h 45 · neuf heures moins le quart<br>12 h · midi · 0 h · minuit</p></div>' +
           '<div class="card" style="background:#fff"><b>🗓️ La date (M3, M11)</b><p class="sm">lundi · mardi · mercredi · jeudi · vendredi · samedi · dimanche</p><p class="sm">janvier · février · mars · avril · mai · juin · juillet · août · septembre · octobre · novembre · décembre</p><p class="sm">le 5 mars 2011 = 05/03/2011 · le 1<sup>er</sup> mai</p></div>' +
           '<div class="card" style="background:#fff"><b>💶 L\'argent (M7)</b><p class="sm">1 € = 100 centimes<br>3,50 € = trois euros cinquante<br>Combien ça coûte ? · C\'est combien ?<br>Ça fait combien ? · Voici 10 €.<br>Je paie en espèces / par carte.</p><p class="sm"><b>Saisons (M8)</b> : le printemps · l\'été · l\'automne · l\'hiver</p></div></div>', "Mémo nombres", levels=False)

    # 5. Consignes en images
    keys = list(PICTO_LABEL.keys())
    b.page(head("Les consignes en images", "Les pictogrammes du cahier : je regarde l'image, je sais quoi faire.") +
           '<div class="grid4">' + "".join(f'<div class="card flex" style="padding:2mm;gap:2mm">{picto(k, 40)}<b class="sm">{PICTO_LABEL[k]}</b></div>' for k in keys) + '</div>' +
           '<h3 class="mt4">Les ateliers et les niveaux</h3><div class="flex" style="flex-wrap:wrap;gap:2mm">' + "".join(f'<span class="atl {k}" style="font-size:11pt;padding:1.5mm 3mm">{v}</span>' for k, v in ATELIERS.items()) + '<span class="alpha-tag" style="font-size:11pt">★ ALPHA</span></div>' +
           f'<p class="mt2">{dots(1)} découverte · {dots(2)} entraînement · {dots(3)} défi · 📌 leçon à étudier · 🔁 je révise · 📄 document de la vie · 🎒 français de l\'école</p>', "Mémo consignes", levels=False)
    return b


if __name__ == "__main__":
    from lib.render import to_pdf
    b = build_annexes()
    to_pdf(b.html(), '/home/claude/syllabus/out/tmp_annexes.pdf')
    print(b.n)
