# Indexing et slicing

print("Hello world"[0])
print("Hello world"[0:5])
print("Hello world"[:5])
print("Hello world"[5:])
print("Begin with the end in mind"[-4])
print("Begin with the end in mind"[-4:])

# Majuscule

print("le texte de mon paragraphe".capitalize())
print("Sarkozy Hollande Sarkozy".replace("Sarkozy", "Macron"))
print(
    "Sarkozy Hollande Sarkozy".find("Sarkozy")
)  # Trouve le premier caractère qui apparait
print("Sarkozy Hollande Sarkozy".count("Sarkozy"))
print("Sarkozy Hollande Sarkozy".lower())
print("Sarkozy Hollande Sarkozy".upper())
print("Sarkozy Hollande Sarkozy".upper().lower())

# Uniformisation des identifiants

print(str(1).zfill(2))
print(str(10).zfill(2))
print(str(100).zfill(2))

# Remplacer une valeur par une autre

print("drilling_speed_miles_per_day".replace("miles", "kilometers"))


# Exercice

print("31555821AB0509"[8:10])
print("31555821AB0509"[-6:-4])

print("ceci est une phrase".capitalize())
print(str("7").zfill(3))
print("PYTHON".lower().capitalize())
print("President Trump".replace("Trump", "Biden"))

# Découpage des dates

print("2023/12/26".split("/"))
print("2023-12-26".split("-"))


# Mettre un triple """ pour exploiter les longs textes

print(
    """> Mes chers amis, Dans ce moment que chacun devine si important pour la France, si important pour l'avenir de chacune de vos familles, si important pour moi, plus que n'importe quel autre sentiment, ce qui m'étreint surtout c'est une émotion profonde. Cette émotion, j'aurais pu essayer de la qualifier, j'aurais pu l'exprimer dans un mot, j'aurais pu vous dire merci mais ce merci n'aurait pas été à la hauteur de ce que j'éprouve en cet instant. Il y a des sentiments qui sont si forts qu'il n'y a pas de mot assez grand pour les dire. Il y a des sentiments qui se ressentent tellement qu'on n'a pas besoin de les nommer.
>
>
> Cette émotion qui me submerge au moment où je vous parle, je vous demande de la recevoir simplement comme un témoignage de ma sincérité, de ma vérité, de mon amitié.
>
> A l'orée de cette campagne où pendant des semaines je vais beaucoup donner, beaucoup recevoir et, peutêtre, beaucoup payer- je veux que chacun d'entre vous soit convaincu de la farouche détermination, de l'énergie infinie que j'irai puiser dans la part la plus profonde de moi-même pour faire triompher la cause qui nous unit tous. Je le sais aujourd'hui, je n'ai pas le droit de vous décevoir, pas le droit d'hésiter, tout simplement pas le droit d'échouer ! Toute ma vie j'ai rêvé d'être utile à la France, à mon pays, à ma patrie. Aujourd'hui vous venez de réaliser la première étape de ce rêve. Seule compte à cet instant l'espérance de la foule immense que vous formez, tendue vers un seul but  :  la victoire de la France. Seul compte l'enthousiasme de cette grande famille qui est la tienne Cher Alain JUPPE. Sans toi et sans la victoire de Jacques CHIRAC en 2002 elle n'aurait jamais existé.
>
> Oui, mes chers amis, tous ensemble réunis, unis, solidaires, tout devient possible.
>
> A cet instant où pour moi tout change, je ne peux m'empêcher de penser à ceux qui m'ont fait rêver d'une autre destinée, d'une vie plus grande, d'un avenir plus passionnant. Ils ont été pour moi une source de réflexion, d'espérance, et même parfois de confiance.
>
> Eux, ce sont les héros de la Résistance et de la France Libre, ces hommes avec lesquels j'ai fait mes premiers pas en politique, ces hommes qui venaient d'une époque où la politique s'était confondue avec le patriotisme et l'épopée. Ils avaient maintenu l'honneur de la France. Ils l'avaient reconstruite, ils l'avaient réconciliée avec l'Allemagne. Ils avaient fait l'Europe, fondé la Vème République. Ils avaient toujours été en avance sur leur temps.
>
> Il m'ont appris, parce qu'ils le savaient mieux que quiconque, ce qu'était le gaullisme  :  non une doctrine que le Général de Gaulle n'avait jamais voulu mais une exigence morale, l'exercice du pouvoir comme un don de soi, la conviction que la France n'est forte que lorsqu'elle est rassemblée, la certitude que rien n'est jamais perdu tant que la flamme de la résistance continue de brûler dans le coeur d'un seul homme, le refus du renoncement, la rupture avec les idées reçues et l'ordre établi quand ils entraînent la France vers le déclin.
>
> Ces hommes furent grands dans la guerre comme dans la paix. Ils avaient toujours fait ce qu'ils devaient faire.
>
> Je veux rendre hommage à Jacques Chaban-Delmas, général de la résistance à 29 ans, au rêve si beau, si prémonitoire, de la Nouvelle Société. Son dernier grand combat politique fut pour moi le premier. J'avais 17 ans et l'impression de partir à la guerre. C'était la fin d'une époque, celle où le gaullisme ne pouvait plus appartenir à un parti.
>
> Je veux rendre hommage à Achille Peretti, grand résistant, qui me confia mon premier mandat de conseiller municipal. Comme je veux dire mon amitié à Edouard Balladur qui m'a fait confiance en me donnant mes premières responsabilités ministérielles alors que j'étais si jeune encore. Je veux dire mon respect à Jacques CHIRAC qui en 1975 à Nice m'a offert mon premier discours.
>
> Ils m'ont enseigné, à moi petit Français au sang mêlé, l'amour de la France et la fierté d'être français. Cet amour n'a jamais faibli et cette fierté ne m'a jamais quittée. Longtemps ce sont des choses que j'ai tues.
>
> Longtemps ce sont des sentiments que j'ai gardés pour moi, comme un trésor caché au fond de mon coeur que je n'éprouvais le besoin de partager avec personne. Je pensais que la politique n'avait rien à voir avec mes émotions personnelles. J'imaginais qu'un homme fort se devait de dissimuler ses émotions. J'ai depuis compris qu'est fort celui qui apparaît dans sa vérité. J'ai compris que l'humanité est une force pas une faiblesse.
>
> J'ai changé. J'ai changé parce qu'à l'instant même où vous m'avez désigné j'ai cessé d'être l'homme d'un seul parti, fût-il le premier de France. J'ai changé parce que l'élection présidentielle est une épreuve de vérité à laquelle nul ne peut se soustraire. Parce que cette vérité je vous la dois. Parce que cette vérité je la dois aux Français.
>
> J'ai changé parce que les épreuves de la vie m'ont changé. Je veux le dire avec pudeur mais je veux le dire parce que c'est la vérité et parce qu'on ne peut pas comprendre la peine de l'autre si on ne l'a pas éprouvée soi-même.
>
> On ne peut pas partager la souffrance de celui qui connaît un échec professionnel ou une déchirure personnelle si on n'a pas souffert soi-même. J'ai connu l'échec, et j'ai dû le surmonter.
>
> On ne peut pas tendre la main à celui qui a perdu tout espoir si l'on n'a jamais douté. Il m'est arrivé de douter. N'est pas courageux celui qui n'a jamais eu peur. Car le courage c'est de surmonter sa peur.
>
> Cette part d'humanité, je l'ai enfouie en moi parce que j'ai longtemps pensé que pour être fort il ne fallait pas montrer ses faiblesses. Aujourd'hui j'ai compris que ce sont les faiblesses, les peines, les échecs qui rendent plus fort. Qu'ils sont les compagnons de celui qui veut aller loin.
>
> J'ai changé parce que le pouvoir m'a changé. Parce qu'il m'a fait ressentir l'écrasante responsabilité morale de la politique. Le mot "morale" ne me fait pas peur.
>
> J'ai changé parce que nul ne peut rester le même devant le visage accablé des parents d'une jeune fille brûlée vive. Parce que nul ne peut rester le même devant la douleur qu'éprouve le mari d'une jeune femme tuée par un multirécidiviste condamné dix fois pour violences et déjà une fois pour meurtre. Dans son regard on lit l'incompréhension de celui qui ne comprend pas comment l'indicible a pu être possible. Je suis révolté par l'injustice et c'en est une lorsque la société ignore les victimes. Je veux parler pour elles, agir pour elles et même, même s'il le faut crier en leurs noms.
>
> J'ai changé parce qu'on change forcément quand on est confronté à l'angoisse de l'ouvrier qui a peur que son usine ferme.
>
> J'ai changé quand j'ai visité le mémorial de Yad Vashem dédié aux victimes de la Shoah. Je me souviens, au bout d'un long couloir, d'une grande pièce avec des milliers de petites lumières et des prénoms d'enfants de 2 ans, de 4 ans, de 5 ans prononcés à voix basse de façon ininterrompue. C'était le murmure des âmes innocentes. Je me suis dit alors que c'était cela la politique  :  faire barrage à la folie des hommes en refusant de se laisser emporter par elle.
>
> J'ai changé quand j'ai lu à Tibhirine le testament bouleversant de frère Christian, enlevé puis égorgé par des fanatiques avec six autres moines de son monastère. Le GIA avait prévenu  :  " nous égorgerons ". On retrouva les sept têtes des moines suppliciés sans leurs corps.
>
> Deux ans auparavant, cet homme de charité avait par avance pardonné à son assassin  :  " s'il m'arrivait un jour d'être victime du terrorisme, (…). Voici que je pourrai, s'il plaît à Dieu, plonger mon regard dans celui du Père pour contempler avec lui les enfants de l'Islam tels qu'il les voit (…). Et toi aussi l'ami de la dernière minute, qui n'aura pas su ce que tu faisais. Oui pour toi aussi je le veux, ce Merci, cet " A-Dieu " (…). Et qu'il nous soit donné de nous retrouver, larrons heureux, en paradis s'il plaît à Dieu notre Père à tous deux ! " Par son humanité immense, par sa volonté de rassembler les hommes le frère Christian fait honneur à la France laïque et républicaine.
>
> A Tibhirine, j'ai compris ce qu'est la force invincible de l'amour et le sens véritable du mot " tolérance ".
>
> A Tibhirine, le frère Christian m'a enseigné, par-delà la mort, que ce que les grandes religions peuvent engendrer de meilleur est plus grand ce qu'elles peuvent engendrer de pire, que les extrémismes et les intégrismes ne doivent jamais être confondus avec le sentiment religieux qui porte une part de l'espérance humaine.
>
> Opposer ce sentiment religieux à la morale laïque serait absurde. Nous sommes les héritiers de deux mille ans de chrétienté et d'un patrimoine de valeurs spirituelles que la morale laïque a incorporé. La laïcité à laquelle je crois, ce n'est pas le combat contre la religion. C'est le respect de toutes les religions.
>
> J'ai changé quand j'ai rencontré Mandel, ce grand Français. J'avais voulu écrire sa vie pour réparer une injustice, pour changer le regard des autres sur cette destinée tragique. C'est mon regard sur la politique qui s'en est trouvé transformé. Georges Mandel avait la passion de la politique. En mars 1940, il est ministre de l'Intérieur.
>
> Au milieu de la débâcle, il est l'un de ceux qui plaident pour la Résistance. Il est arrêté. Le 7 juillet 1944, des miliciens le tirent de sa prison et le font monter dans une voiture. Arrivé dans la forêt de Fontainebleau ils l'abattent d'une rafale de mitraillette.
>
> Le 24 juillet, sa fille écrit à Pierre Laval  :  " Je suis encore bien petite et bien faible à côté de vous (…). Je veux vous dire M. Laval que je plains beaucoup votre fille. Vous allez lui laisser un nom qui marquera dans l'histoire. Le mien aussi. Seulement le mien sera celui d'un martyr." Ce jour-là, la France s'appelle Claude Mandel. Elle a 14 ans, son père vient d'être assassiné non par l'occupant mais par des Français ennemis de la France.
>
> La France, elle a 17 ans le visage de Guy Môquet quand il est fusillé  :  " 17 ans et demi… Ma vie a été courte ! Je n'ai aucun regret si ce n'est de vous quitter tous. " La France, elle a 19 ans et le visage lumineux d'une fille de Lorraine quand Jeanne comparaît devant ses juges.
>
> Elle a 32 ans et le visage d'un émigré italien naturalisé français, quand Gambetta quitte en ballon Paris assiégé pour organiser la résistance aux Prussiens.
>
> La France, elle a 44 ans, le visage ensanglanté de Moulin quand il meurt sous la torture " sans avoir livré aucun secret, lui qui les savait tous. " Elle a 50 ans et la voix du Général de Gaulle le 18 juin 1940.
>
> Elle a 56 ans, le visage noir d'un petit-fils d'esclave devenu gouverneur du Tchad et premier résistant de la France d'Outre-Mer. Elle s'appelle Félix Eboué.
>
> Elle a 58 ans et le visage de Zola quand il signe "J'accuse" pour défendre Dreyfus et la Justice.
>
> Elle a 60 ans, le visage d'un proscrit qui s'appelle Victor Hugo lorsqu'au commencement des Misérables il écrit  :  " Tant qu'il y aura sur la Terre ignorance et misère des livres de la nature de celui-ci pourront ne pas être inutiles ".
>
> Elle a 77 ans et la force du Tigre quand Clemenceau déclare en mars 1918  :  " Je continue à faire la guerre et je continuerai jusqu'au dernier quart d'heure car c'est nous qui aurons le dernier quart d'heure ! " Elle a la voix, la figure, la dignité d'une femme, d'une mère, rescapée des camps de la mort qui s'écrie à la tribune de l'Assemblée  :  "nous ne pouvons plus fermer les yeux sur les 300 000 avortements qui, chaque année mutilent les femmes de ce pays". Ce jour là, elle s'appelle Simone Veil.
>
> Elle a la voix d'un jeune prêtre français, l'abbé Pierre, qui à la radio un jour de l'hiver 54 lance aux hommes son appel pathétique  :  " Mes amis au secours. Une femme vient de mourir gelée cette nuit, à trois heures, sur le trottoir du boulevard Sébastopol (…). Devant leurs frères mourant de misère, une seule opinion doit exister entre les hommes  :  la volonté de rendre impossible que cela dure (…).
>
> Elle a le visage, l'âge de Georges Pompidou quand il évite le pire en mai 68.
>
> La France, elle a le visage, l'âge, la voix de tous ceux qui ont cru en elle, qui se sont battus pour elle, pour son idéal, pour ses valeurs, pour sa liberté.
>
> Elle a le visage, l'âge, la voix de tous les Français qui ont au fond de leur coeur la conviction que la France n'est pas finie. Car elle n'est pas finie la France. Parce que dans mon coeur comme dans mon esprit, la France ne veut pas, ne doit pas, ne peut pas mourir.
>
> A chaque fois qu'on l'a crue finie, elle a étonné le monde. A chaque fois elle s'est relevée. A chaque fois elle a su trouver en elle la force de ressusciter.
>
> Ma France, c'est le pays qui a fait la synthèse entre l'Ancien Régime et la Révolution, entre l'Etat capétien et l'Etat républicain, qui a inventé la laïcité pour faire vivre ensemble ceux qui croient au Ciel et ceux qui n'y croient pas.
>
> Ma France, c'est le pays qui, entre le drapeau blanc et le drapeau rouge a choisi le drapeau tricolore, en a fait le drapeau de la liberté et l'a couvert de gloire.
>
> Ma France, c'est celle de tous les Français sans exception. C'est la France de Saint-Louis et celle de Carnot, celle des croisades et de Valmy. Celle de Pascal et de Voltaire. Celles des cathédrales et de l'Encyclopédie.
>
> Celle d'Henri IV et de l'Edit de Nantes. Celle des droits de l'homme et de la liberté de conscience.
>
> Ma France, c'est celle des Français qui votent pour les extrêmes non parce qu'ils croient à leurs idées mais parce qu'ils désespèrent de se faire entendre. Je veux leur tendre la main.
>
> Ma France, c'est celle des travailleurs qui ont cru à la gauche de Jaurès et de Blum et qui ne se reconnaissent pas dans la gauche immobile qui ne respecte plus le travail. Je veux leur tendre la main.
>
> Ma France, c'est celle de tous ceux qui ne croient plus à la politique parce qu'elle leur a si souvent menti. Je veux leur dire  :  aidez-moi à rompre avec la politique qui vous a déçu pour renouer avec l'espérance.
>
> Ma France, c'est celle de tous ces Français qui ne savent pas très bien au fond s'ils sont de droite, de gauche ou du centre parce qu'ils sont avant tout de bonne volonté. Je veux leur dire par-delà les engagements partisans que j'ai besoin d'eux pour que tout devienne possible.
>
> Bien sûr il y a la droite et il y a la gauche. Mes valeurs sont les vôtres, celles de la droite républicaine. Ce sont des valeurs d'équité, d'ordre, de mérite, de travail, de responsabilité. Je les assume. Mais dans les valeurs auxquelles je crois, il y a aussi le mouvement. Je ne suis pas un conservateur. Je ne veux pas d'une France immobile. Je veux l'innovation, la création, la lutte contre les injustices. J'ai voulu faire entrer ces idées dans le patrimoine de la droite républicaine alors même que la gauche les délaissait.
>
> Mais au-delà de la droite et de la gauche, il y a la République qui doit être irréprochable parce qu'elle est le bien de tous. Il y a l'Etat qui doit être impartial. Il y a la France qui est une destinée commune.
>
> Etre de droite c'est refuser de parler au nom d'une France contre une autre. C'est refuser la lutte des classes.
>
> C'est refuser de chercher dans l'idéologie la réponse à toutes les questions, la solution à tous les problèmes.
>
> C'est refuser de voir dans le contradicteur un ennemi mais un citoyen dont on doit entendre les arguments.
>
> Ma France, c'est une nation ouverte, accueillante, c'est la patrie des droits de l'homme. C'est elle qui m'a fait ce que je suis. J'aime passionnément le pays qui m'a vu naître. Je n'accepte pas de le voir dénigrer. Je n'accepte pas qu'on veuille habiter en France sans respecter et sans aimer la France. Je n'accepte pas qu'on veuille s'installer en France sans se donner la peine de parler et d'écrire le Français.
>
> Je respecte toutes les cultures à travers le monde. Mais qu'il soit entendu que si on vit en France alors on respecte les valeurs et les lois de la République.
>
> La soumission de la femme c'est le contraire de la République, ceux qui veulent soumettre leurs femmes n'ont rien à faire en France. La polygamie c'est le contraire de la République. Les polygames n'ont rien à faire en France. L'excision c'est une atteinte à la dignité de la femme, c'est le contraire de la République, ceux qui veulent la pratiquer sur leurs enfants ne sont pas les bienvenus sur le territoire de la République française.
>
> Ma France, c'est une nation qui revendique son identité, qui assume son histoire. On ne construit rien sur la haine des autres, mais on ne construit pas davantage sur la haine de soi. On ne construit rien en demandant aux enfants d'expier les fautes de leurs pères.
>
> De Gaulle n'a pas dit à la jeunesse allemande  :  " vous êtes coupables des crimes de vos pères ". Il lui a dit  :  " je vous félicite d'être les enfants d'un grand peuple, qui parfois au cours de son histoire a commis de grandes fautes ".
>
> Au peuple de notre ancien empire nous devons offrir non l'expiation mais la fraternité.
>
> A tous ceux qui veulent devenir Français nous offrons non de nous repentir mais de partager la liberté, l'égalité et la fierté d'être Français. Gardons-nous de juger trop sévèrement le passé avec les yeux du présent.
>
> Tous les Français durant la guerre n'étaient pas pétainistes. Les pêcheurs de l'île de Sein, les paysans du Vercors n'étaient pas pétainistes. Les paysans du Périgord qui cachaient au péril de leur vie les Juifs de Strasbourg n'étaient pas pétainistes. Tous les Français dans les colonies n'étaient pas des exploiteurs. Il y avait aussi parmi eux de petites gens qui travaillaient dur, qui n'exploitaient personne et qui ont tout perdu.
>
> Français, prompts à détester votre pays et son histoire, écoutez la grande voix de Jaurès :  " Ce qu'il faut ce n'est pas juger toujours, juger tout le temps, c'est se demander d'époque en époque, de génération en génération, de quels moyens de vie disposaient les hommes, à quelles difficultés ils étaient en proie, quel était le péril ou la pesanteur de leur tâche, et rendre justice à chacun sous le fardeau. " Pourquoi la gauche n'entend-elle plus la voix de Jaurès ? Comment penser que l'on pourra un jour faire aimer ce que l'on aura appris à détester ? Au bout du chemin de la repentance et de la détestation de soi il y a, ne nous y trompons pas, le communautarisme et la loi des tribus. Je refuse le communautarisme qui réduit l'homme à sa seule identité visible. Je combats la loi des tribus parce que c'est la loi de la force brutale et systématique.
>
> Il ne s'agit pour personne d'oublier sa propre histoire. Les enfants des républicains espagnols parqués dans des camps de réfugiés, les enfants des Juifs persécutés par la Milice, les descendants des camisards des Cévennes, les fils des harkis n'ont rien oublié de leur histoire. Mais ils ont pris, comme moi, fils d'immigré, la culture, la langue et l'histoire de la France en partage, pour pouvoir mieux vivre une destinée commune.
>
> Face au drame algérien, Camus avait dit  :  " Les grandes tragédies de l'histoire fascinent souvent les hommes par leurs visages horribles. Ils restent alors immobiles devant elles sans pouvoir se décider à rien qu'à attendre. " Attendre quoi ? Sinon le pire ? Il avait ajouté  :  " La force du coeur, l'intelligence, le courage suffisent pourtant pour faire échec au destin ".
>
> Pourquoi la gauche n'entend-elle plus la voix de Camus ? Qui ne voit qu'une fois encore avec du coeur, de l'intelligence et du courage la clé de notre unité et de notre avenir est dans la République et dans la démocratie ? * Depuis le premier jour où elle est apparue dans notre histoire, la République est un combat toujours recommencé pour l'émancipation de l'homme. La République commence quand la politique cesse d'être au service de la volonté de puissance pour se mettre au service du bonheur des hommes.
>
> Le but de la République c'est d'arracher du coeur de chacun le sentiment de l'injustice.
>
> Le but de la République c'est de permettre à celui qui n'a rien d'être quand même un homme libre, à celui qui travaille de posséder quelque chose, à celui qui commence tout en bas de l'échelle sociale de la gravir aussi haut que ses capacités le lui permettent.
>
> Le but de la République c'est que les chances de réussite soient égales pour tous. C'est que l'enfant soit éduqué, le malade soigné, le vieillard arraché à la solitude, le travailleur respecté, la misère vaincue.
>
> Le but de la République c'est la reconnaissance du travail comme source de la propriété et la propriété comme représentation du travail.
>
> La République de Jules Ferry n'était pas celle de Danton. Celle du Général De Gaulle n'était pas celle de Jules Ferry. Mais c'était toujours le même idéal poursuivi par des moyens différents. La République n'est pas une religion. La République n'est pas un dogme. La République est un projet toujours inachevé.
>
> Si nous voulons que la République redevienne un projet partagé, il nous faut passer de la République virtuelle à la République réelle.
>
> La République réelle, c'est la République qui ne se contente pas d'inscrire la liberté, l'égalité et la fraternité sur ses monuments, mais qui les inscrit dans la réalité de la vie quotidienne.
>
> La République réelle ce n'est pas la République où tout le monde reçoit la même chose. C'est la République où chacun reçoit selon son mérite ou son handicap.
>
> La République réelle c'est celle qui fait plus pour celui qui veut s'en sortir et qui fait moins pour celui qui ne veut rien faire et dont la société ne peut accepter qu'il vive à son crochet.
>
> La République réelle ce n'est pas la République où il n'y a que des droits et aucun devoir. C'est la République où les devoirs sont la contrepartie des droits. Je propose qu'aucun minimum social ne soit accordé sans la contre-partie d'une activité d'intérêt général.
>
> C'est celle où les hommes et les femmes ont les mêmes droits, les mêmes salaires, les mêmes possibilités de carrière, la même considération.
>
> C'est celle où les mères qui veulent travailler peuvent faire garder leurs enfants, où la maternité n'est pas un handicap pour la vie professionnelle, où les années consacrées à l'éducation des enfants sont prises en compte dans le calcul des retraites.
>
> La République réelle à laquelle je crois c'est celle qui ne reste pas indifférente au sort de l'enfant pauvre, à la souffrance de ceux que la vie n'a pas épargnés. C'est celle qui garde tous les enfants dont les familles le souhaitent en étude surveillée quand les parents ne peuvent pas s'occuper d'eux parce qu'ils travaillent. Celle qui construit des internats d'excellence pour les élèves d'origine modeste parce qu'ils ne peuvent pas étudier chez eux.
>
> La République virtuelle c'est celle qui fait de l'élève l'égal du maître. La République réelle à laquelle je crois c'est celle qui veut une école de l'autorité et du respect où l'élève se lève quand le professeur entre, où les filles ne portent pas le voile, où les garçons ne gardent pas leur casquette en classe.
>
> La République virtuelle c'est celle qui veut donner un diplôme à tout le monde en abaissant le niveau des examens. La République réelle c'est celle qui veut donner une formation à chacun, celle qui n'a peur ni de l'orientation, ni de la sélection, ni de l'élitisme républicain qui est la condition de la promotion sociale. C'est l'école de l'excellence pas l'école du nivellement et de l'égalitarisme.
>
> La République réelle, c'est celle où le sport n'est pas un ghetto réservé aux jeunes ou aux minorités visibles mais devient une école de la vie parce que les valeurs du sport transcendent tous les âges, toutes les différences, toutes les incompréhensions. Parce que le sport c'est une éthique universelle.
>
> La République virtuelle c'est celle qui pratique l'assistanat généralisé mais qui laisse des gens mourir sur le trottoir. C'est celle qui proclame le droit au logement et qui ne construit pas de logements. C'est celle qui proclame le droit à l'emploi et qui renonce à l'objectif du plein emploi. C'est celle qui proclame que le travail est une valeur mais qui fait tout pour le décourager. C'est celle qui proclame la continuité du service public mais accepte que les usagers soient périodiquement les otages des grévistes. C'est celle qui proclame le droit d'aller et de venir mais cherche sans arrêt des excuses aux délinquants qui empoisonnent la vie de tout le monde.
>
> La République réelle c'est celle qui rend effectifs les droits qu'elle proclame.
>
> C'est la République qui crée des emplois, qui construit des logements qui permet au travailleur de vivre de son travail, qui donne sa chance à l'enfant pauvre, qui met les retraités des régimes spéciaux à égalité avec ceux du secteur privé et de la fonction publique, qui garantit le service minimum en cas de grève et qui fait respecter la loi par tout le monde. Je souhaite une loi sur le service minimum dès le mois de juin 2007. Je souhaite en outre qu'une loi impose le vote à bulletins secrets dans les 8 jours du déclenchement d'une grève dans une entreprise, une université, une administration.
>
> Je crois dans la démocratie sociale. Je crois dans le dialogue, dans la négociation, dans le paritarisme. Mais je refuse la prise d'otages, les blocages, les archaïsmes, la violence, la loi du plus fort… et le manque de courage ! La République réelle à laquelle je crois c'est celle qui met en prison l'assassin présumé de Claude Erignac et qui traite les cagoulés et les poseurs de bombes pour ce qu'ils sont  :  des meurtriers et des lâches.
>
> La République réelle c'est celle qui se donne une obligation de résultat. C'est celle des droits que l'on peut faire valoir devant les tribunaux parce que l'on s'est donné les moyens de les rendre opposables.
>
> Ma République c'est celle du droit opposable à l'hébergement, parce que si l'on pense que la politique ne peut rien faire dans un pays comme la France pour empêcher les gens de mourir sur le trottoir, il ne faut pas faire de politique.
>
> Ma République c'est celle du droit opposable au logement, parce que si l'on pense que la politique ne peut rien faire pour résoudre en dix ans la crise du logement en construisant les 700 000 logements qui manquent, il ne faut pas faire de politique. Ma République est celle où chacun pourra accéder à la propriété de son logement. Il faut permettre aux classes moyennes, à la France qui travaille d'accéder à la propriété. Je propose que l'Etat garantisse l'emprunt de celui qui n'a pas de relations. Je propose que l'on puisse déduire tous les intérêts de son emprunt du revenu imposable. Je propose que l'on fasse de la France un pays de propriétaires parce que lorsque l'on a accédé à la propriété on respecte son immeuble, son quartier, son environnement… et donc les autres. Parce que lorsque l'on a accédé à la propriété on est moins vulnérable aux accidents de la vie.
>
> Ma République c'est celle du droit opposable à la garde d'enfants, parce que lorsqu'on pense que la politique ne peut rien faire pour résoudre en cinq ans le problème des femmes qui travaillent et qui n'arrivent pas à faire garder leurs enfants, il ne faut pas faire de politique.
>
> Ma République c'est celle du droit opposable à la scolarisation des enfants handicapés, parce que si l'on pense que d'ici à cinq ans on ne peut pas trouver les moyens de scolariser tous les enfants handicapés, il ne faut pas faire de politique. Ce droit n'est pas seulement un droit pour les enfants handicapés, c'est aussi une chance pour les autres enfants.
>
> Mais ma République c'est aussi celle des devoirs opposables .Nous ne pouvons nous montrer complaisants avec le développement des fraudes des abus et des gaspillages qui sont une insulte au travail des français et qui sape les fondements de la solidarité nationale. Les droits ne vont pas sans les devoirs, et l'on ne peut valablement aider que ceux qui respectent les règles et consentent à faire un effort pour s'en sortir.
>
> Je veux être le Président d'une République qui dira aux jeunes  :  " vous voulez être reconnus comme des citoyens à part entière dès que vous devenez majeurs. Vous le serez. Vous aurez les moyens de décider par vous-mêmes quand vous quitterez le domicile de vos parents. Vous aurez les moyens de réaliser vos ambitions, de vivre votre vie comme vous le souhaitez, d'aimer comme vous l'entendez. Vous aurez les moyens de devenir ce que vous voulez devenir. Mais vous accepterez d'apprendre et de vous formez, vous serez apprenti, vous serez stagiaire, vous serez étudiant. Si vous avez quitté l'école jeune vous pourrez aller dans une école de la deuxième chance. Si vous n'avez pas le bac vous pourrez accéder à des cursus qui vous permettrons quand même d'entrer à l'université. En contrepartie les aides qui sont aujourd'hui versées à votre famille pour votre éducation vous serons versées à vous, si vous le souhaitez. Si vous en avez besoin, vous recevrez une allocation de formation de 300 euros par mois qui vous sera supprimée si vous n'êtes pas assidu à votre formation, si vous cessez d'étudier sérieusement. Vous aurez le droit d'emprunter à taux zéro avec la garantie de l'Etat pour financer ton projet personnel et vous commencerez à rembourser cet emprunt à partir du moment où vous aurez obtenu votre premier emploi. Si vous y ajoutez un petit travail – et tout sera fait pour que chaque étudiant puisse étudier et travailler en même temps – Vous aurez une véritable autonomie financière qui est la clé de toute liberté. Mais vous la mériterez par votre effort, par votre travail, par votre assiduité, par votre sérieux. Vous deviendrez responsable de votre vie.
>
> Je ne veux pas de la société du minimum parce qu'avec le minimum on ne vit pas. On survit. Je veux une société du maximum. Je préfère une jeunesse à qui l'on donne la possibilité de réaliser ses projets plutôt qu'une jeunesse qui est condamnée à l'assistanat.
>
> Je veux être le Président d'une République qui dit à la jeunesse  :  " tu reçois beaucoup, tu dois donner aussi de toi-même. Tu dois comprendre que tu appartiens à une nation, qui espère en toi et à laquelle tu dois beaucoup parce que c'est elle qui te fait libre. C'est pourquoi, je propose un service civique obligatoire de 6 mois que chacun modulera en fonction de ses propres contraintes d'études, de projet professionnel, de vie familiale. Ce sera pour toi une opportunité de t'engager dans de grandes causes humanitaires, d'élargir ton horizon, de rencontrer d'autres jeunes qui sont différents de toi, ce sera une possibilité de réinsertion dans la société pour des jeunes qui en auraient été exclus.
>
> Notre modèle républicain est en crise. Cette crise est avant tout morale. Au coeur de celle-ci il y a la dévalorisation du travail.
>
> Le travail c'est la liberté, c'est l'égalité des chances, c'est la promotion sociale. Le travail c'est le respect, c'est la dignité, c'est la citoyenneté réelle. Avec la crise de la valeur travail, c'est l'espérance qui disparaît.
>
> Comment espérer encore si le travail ne permet plus de se mettre à l'abri de la précarité, de s'en sortir, de progresser ? Le travailleur qui voit l'assisté s'en tirer mieux que lui pour boucler ses fins de mois sans rien faire ou le patron qui a conduit son entreprise au bord de la faillite partir avec un parachute en or finit par se dire qu'il n'a aucune raison de se donner autant de mal.
>
> Le travail est dévalorisé, la France qui travaille est démoralisée.
>
> Le problème c'est que la France travaille moins quand les autres travaillent plus. Le plein emploi est possible chez les autres. Il l'est aussi chez nous. Il faut aimer le travail et pas le détester.
>
> Le problème c'est qu'il n'y a pas assez de travail en France pour financer les retraites, l'allongement de la durée de la vie, la dépendance, la protection sociale, pour faire fonctionner notre modèle d'intégration.
>
> Longtemps la droite a ignoré le travailleur et la gauche qui jadis s'identifiait à lui a fini par le trahir.
>
> Je veux être le Président d'une France qui remettra le travailleur au coeur de la société. Je veux proposer aux Français une politique dont le but sera la revalorisation du travail.
>
> Quand on facilite l'endettement des ménages pour financer les créations d'entreprises ou l'achat d'une voiture indispensable pour aller travailler, on favorise le travail. Je veux créer un système de cautionnement public qui mutualise les risques et permette d'emprunter à tous ceux qui ont un projet.
>
> Quand on investit plus on construit un avenir pour les travailleurs. C'est pourquoi je veux porter le crédit d'impôt recherche à 100%. C'est pourquoi je veux que les entreprises qui investissent et qui créent des emplois paient moins d'impôt sur les bénéfices. C'est pourquoi je veux que l'Etat se donne les moyens d'investir dans les bassins économiques en déclin pour les réindustrialiser et non pas seulement pour financer des départs à la retraite anticipés.
>
> Quand les entreprises savent qu'elles pourront licencier en cas de difficulté, elles embauchent plus facilement. Je veux protéger les personnes plutôt que les emplois. Je veux sécuriser les parcours professionnels plutôt qu'empêcher les licenciements. Je veux créer un contrat unique à durée indéterminée qui remplacera les contrats précaires et qui permettra aux salariés d'acquérir progressivement des droits. Je veux que les bas salaires soient garantis en cas de perte d'emploi, en contrepartie de l'obligation de ne pas refuser plus de deux offres d'emplois successives. Quand on est indemnisé par la société on doit accepter l'offre d'emploi correspondant à vos qualifications qui vous est proposée.
>
> Le travail n'est pas assez récompensé, valorisé, respecté. Et c'est pour cela que le pouvoir d'achat est trop faible car les salaires sont trop bas et les charges trop lourdes.
>
> Il faut augmenter le pouvoir d'achat. Les socialistes promettront de travailler moins, moi je veux que les Français gagnent plus. Je veux être le Président de l'augmentation du pouvoir d'achat. Je veux être celui qui vous garantit que si vous travaillez plus, si vous prenez plus de risque, si vous vous engagez plus, vous gagnerez davantage. Je veux être le Président du peuple qui a bien compris que les RTT ne servent à rien si on n'a pas de quoi payer des vacances à ses enfants. Je veux l'exonération de charges sociales et de l'impôt sur le revenu pour les heures supplémentaires pour qu'enfin on comprenne en France que le travail est une émancipation, que c'est le chômage qui est une aliénation.
>
> C'est pour cela que je veux que chaque Français puisse transmettre en franchise d'impôt sur les successions le fruit d'une vie de labeur. On n'a pas à s'excuser d'avoir un patrimoine en contrepartie de son travail. La France doit accueillir les patrimoines et pas les faire fuir. Quand il y a moins de richesses dans un pays ce sont les plus pauvres qui en pâtissent. Partager ce qu'on n'a plus ne fait pas la prospérité d'un peuple.
>
> Je veux que l'Etat soit contraint de laisser à chacun au moins la moitié de ce qu'il à gagné. Je veux un bouclier fiscal à 50% y compris la CSG et la CRDS.
>
> Tout vaut mieux que de taxer l'homme au travail.
>
> Tout vaut mieux que de taxer le travailleur qui crée la richesse.
>
> Je veux taxer le pollueur plutôt que le travailleur.
>
> Je veux taxer les importations qui ne respectent pas les normes internationales plutôt que le travail.
>
> Je préfère taxer la consommation plutôt que l'emploi.
>
> C'est le travail qui crée le travail. Le travail contribuera à rééquilibrer nos finances publiques. Il refera de la France une République fraternelle.
>
> Je veux être le Président de tous ces Français qui pensent que l'assistanat est dégradant pour la personne humaine. Je veux être le Président qui s'efforcera de moraliser le capitalisme parce que je ne crois pas à la survie d'un capitalisme sans morale et sans éthique, parce que je ne crois pas à la survie d'un capitalisme où ceux qui échouent gagneraient davantage que ceux qui réussissent, parce que je ne crois pas à la survie d'un capitalisme où tous les profits seraient accaparés et où, à l'inverse, tous les impôts seraient partagés Je veux être le Président qui va remettre la morale au coeur de la politique. L'enfant qui n'apprend à l'école ni la morale, ni l'instruction civique ne comprendra pas plus tard qu'être citoyen ne signifie pas seulement avoir des droits. Le jeune qui ne fait plus son service militaire croit de bonne foi qu'il n'aura jamais rien à donner aux autres en contrepartie de ce qu'il reçoit. L'honnête homme qui voit le délinquant rester impuni et une partie de ses impôts aller dans la poches du fraudeur finira par se demander pourquoi il devrait être le seul à être honnête.
>
> Mais si l'école n'apprend plus la citoyenneté, ce n'est pas la faute des enseignants. Si l'Etat va mal ce n'est pas de la faute des fonctionnaires. C'est la politique qui est responsable.
>
> Je n'aime pas la manière dont on parle des fonctionnaires dans notre pays. Je n'aime pas la politique qui cherche à opposer les salariés du privé à ceux du public. Ils ont pour la plupart une haute idée de leur mission. Les fonctionnaires sont démotivés parce que leur travail n'est pas reconnu, parce que ceux qui font le moins gagnent autant que ceux qui font le plus. Ils sont démoralisés parce que les 35 heures ont tout compliqué. Il faut aller voir dans les hôpitaux le désarroi et la peine de ces infirmières, de ces aidessoignantes aux prises avec la désorganisation et le manque de personnel que la réduction autoritaire du temps de travail a engendrés.
>
> Je veux un Etat où les fonctionnaires seront moins nombreux mais mieux payés, où ils pourront gagner davantage quand ils travailleront plus, où les gains de productivité seront équitablement partagés, où le mérite individuel sera récompensé, où la promotion interne sera facilitée, où l'infirmière pourra devenir médecin, où le technicien pourra devenir ingénieur, où l'agent administratif pourra devenir Directeur, où la dignité et la protection des agents publics seront garanties.
>
> Je veux que la fonction publique cesse d'être un refuge pour ceux qui ont peur de prendre des risques. Je veux qu'elle redevienne une vocation pour ceux qui ont le goût du bien commun et du service public.
>
> Je veux une démocratie irréprochable.
>
> La démocratie irréprochable c'est la participation de chacun à la définition du destin de tous.
>
> La démocratie irréprochable c'est celle où il n'est pas nécessaire de voter pour les extrêmes pour se faire entendre. Celle où il n'est pas nécessaire de descendre dans la rue pour crier son désespoir. Celle où chacun reconnaît dans la politique de son pays une part de lui-même.
>
> La démocratie irréprochable ce n'est pas celle où l'enfant d'un de ces quartiers dans lesquels s'accumulent toutes les difficultés qui regarde la télévision trouve qu'aucun homme politique ne lui ressemble.
>
> La démocratie irréprochable c'est celle qui permet aux enfants de tous les quartiers de ressentir qu'ils ont quelque chose en commun.
>
> La démocratie irréprochable c'est celle qui permet d'arracher le poison de l'extrémisme du coeur de tous ceux qui se laissent entraîner par leur colère et par leur peur parce qu'ils se sentent exclus.
>
> La démocratie irréprochable ce n'est pas une démocratie où les nominations se décident en fonction des connivences et des amitiés mais en fonction des compétences. C'est celle dans laquelle l'Etat est impartial.
>
> Si l'Etat veut être respecté, il doit être respectable. Je ne transigerai pas. Pour certains postes il ne doit pas y avoir de nomination sans qu'au préalable celui que l'on envisage de nommer ne soit contraint d'exposer ses vues stratégiques pour l'entreprise ou l'organisme qu'il veut présider. Et de surcroît cette nomination doit être ratifiée par un vote des commissions parlementaires concernées. Le fait du prince n'est pas compatible avec la République irréprochable.
>
> La démocratie irréprochable ce n'est pas une démocratie où l'exécutif est tout et le Parlement rien. C'est une démocratie où le Parlement contrôle l'exécutif et a les moyens de le faire.
>
> La démocratie irréprochable c'est un Président qui s'explique devant le Parlement. C'est un Président qui gouverne. C'est un président qui assume. On n'élit pas un arbitre mais un leader qui dira avant tout ce qu'il fera et surtout qui fera après tout ce qu'il aura dit ! La démocratie irréprochable ce n'est pas celle où l'indépendance de la justice se confond avec l'irresponsabilité des juges. C'est celle où les juges sont responsables comme n'importe quel autre citoyen des fautes qu'ils commettent. Au moins que le drame d'Outreau ait servi à quelque chose.
>
> La démocratie irréprochable c'est celle où le gouvernement définit la politique pénale et où le peuple participe à la décision de justice. Je souhaite que les jurys populaires jugent certaines affaires correctionnelles comme ils le font déjà dans les procès d'assises.
>
> La démocratie irréprochable c'est celle qui punit durement le crime et qui traite dignement les condamnés. Je veux que nos prisons soient rénovées, trop d'entre elles ne sont pas digne de la France.
>
> Notre démocratie n'a pas besoin d'une nouvelle révolution constitutionnelle. On change trop notre Constitution. Il faut arrêter de dire qu'elle est bonne et proposer tous les trimestres une nouvelle modification. Mais nous devons changer radicalement nos comportements pour aller vers davantage d'impartialité, d'équité, d'honnêteté, de responsabilité, de transparence.
>
> La démocratie irréprochable ce n'est pas celle où la représentativité syndicale est présumée en fonction du comportement patriotique durant la Seconde Guerre Mondiale. C'est celle où la représentativité se prouve dans des élections où chacun peut librement se présenter dès le premier tour.
>
> La démocratie irréprochable ce n'est pas seulement la démocratie Française, c'est aussi la démocratie européenne parce que les deux sont indissolublement liées. Après le " non " au référendum sur la Constitution européenne on ne peut pas continuer à faire l'Europe de la même manière. Je veux être le candidat qui dit à celui qui a voté " oui "  :  " j'ai voté " oui " aussi et comme vous, je crois à une France ouverte sur le monde et à une Europe qui permettra à la France d'être plus grande. Comme vous, je crois que rester immobile serait mortel quand tous les autres avancent. " Mais je veux lui dire aussi qu'il serait plus mortel encore de juger celui qui a voté " non " au lieu de chercher à le comprendre. Je veux lui dire que la France qui gagne perdra tout si elle méprise la France qui ne se sent pas bien. Je veux lui dire que tous nos destins sont liés, que tout ce qui divise les Français affaiblit la France, que tout ce qui affaiblit la France affaiblit chacun d'entre nous. Je veux dire à celui qui n'a pas peur parce que tout va bien pour lui qu'il doit tendre la main à celui qui a peur de l'exclusion, à celui qui vit dans la hantise du déclassement, parce que nul n'est à l'abri des accidents de la vie, parce que notre capacité à vivre ensemble, à nous comprendre et à nous respecter est notre bien le plus précieux.
>
> Je veux être le Président d'une France qui dira aux Européens  :  nous voulons l'Europe, nous la voulons parce que sans elle nos vieilles nations ne pèseront rien dans la mondialisation, sans elle nos valeurs ne pourront pas être défendues, sans elle le choc des civilisations deviendra plus probable et le péril pour l'humanité sera terrible.
>
> Je veux être le Président d'une France qui dira aux Européens  :  " nous ne ressusciterons pas la Constitution européenne. Le Président Giscard d'Estaing a fait un travail remarquable, mais le peuple a tranché.
>
> L'urgence c'est de faire en sorte que l'Europe puisse fonctionner de nouveau en adoptant par la voie parlementaire un traité simplifié. L'urgence est celle d'une Europe qui joue le jeu de la subsidiarité, qui se dote d'un gouvernement économique. C'est celle d'une Europe dans laquelle personne ne peut obliger un Etat à s'engager dans une politique à laquelle il est opposé, mais dans laquelle aussi personne ne peut empêcher les autres d'agir.
>
> L'Europe, je l'imagine comme un multiplicateur de puissance non comme un facteur d'impuissance, comme une protection non comme le cheval de Troie de tous les dumpings, pour agir et non pour subir. Je crois en l'Europe comme la voulaient ses pères fondateurs, comme une volonté commune, non comme un renoncement collectif. Je demeurerai toute ma vie un Européen convaincu. Mais je veux avoir la liberté de dire que l'Europe doit se doter de frontières, que tous les pays du monde n'ont pas vocation à intégrer l'Europe à commencer par la Turquie. A s'élargir sans limite on prend le risque de détruire l'union politique européenne, je ne l'accepterai pas.
>
> Je crois au libre échange et à la concurrence. Mais je veux que cesse la naïveté et que l'on impose la réciprocité dans les négociations commerciales. La concurrence doit être loyale. Ce n'est pas loyal d'imposer à nos entreprises de se battre avec des concurrents qui ne respectent aucune règle environnementale, sociale, morale.
>
> Je veux être le Président d'une France qui dira aux Européens  :  " nous ne pouvons plus continuer avec une monnaie unique sans un gouvernement économique. Nous en pouvons plus continuer avec une Europe sans préférence communautaire, où un pays membre peut décider unilatéralement de régulariser massivement ses immigrés clandestins sans demander l'avis de personne alors que ses frontières sont ouvertes. " Je veux être le Président d'une France fière de ses régions d'Outre-Mer qui sont une chance pour notre nation et qui ont le droit au développement par l'instauration de zones franches globales.
>
> Je veux être le Président d'une France qui ira dire aux Européens  :  " nous ne pouvons pas continuer à tourner le dos à la Méditerranée, car autour de cette mer où depuis deux mille ans la raison et la foi dialoguent et s'affrontent, sur ces rivages où l'on a mis pour la première fois l'homme au centre de l'univers, se joue une fois encore une part essentielle de notre destin. Là nous pouvons tout gagner ou tout perdre. Nous pouvons avoir la paix ou la guerre, la meilleure part de la civilisation mondiale ou le fanatisme, le dialogue des cultures ou l'intolérance et le racisme, la prospérité ou la misère, le développement durable ou la pire des catastrophes écologiques. " Je veux être le Président d'une France qui dira à tous les pays de la Méditerranée  :  " sommes-nous condamnés indéfiniment à la vengeance et à la haine ? Rien ne doit être oublié, mais il nous appartient à tous de forger ici, dans le creuset des siècles et des civilisations, le destin commun de l'Europe, du Moyen-Orient et de l'Afrique, dans une relation d'égalité et de fraternité. " Je veux être le Président d'une France qui proposera d'unir la Méditerranée comme elle a proposé jadis d'unir l'Europe, et qui inscrira dans la perspective de cette unité les relations de l'Europe et de la Turquie, ses liens avec le monde arabe, la recherche d'une issue au conflit israélo-palestinien, mais aussi l'immigration choisie, le codéveloppement, la maîtrise du libre-échange et la défense de la diversité culturelle.
>
> Je veux être le Président d'une France qui dira aux Européens et aux Africains  :  " dans un monde où se dessinent de vastes stratégies continentales qui enjambent les hémisphères, il est vital pour l'Europe d'imaginer une stratégie euro-africaine dont la Méditerranée sera fatalement le pivot ".
>
> Je veux être le Président d'une France qui dira à l'Amérique  :  " nous sommes amis et la France demeurera fidèle à cette amitié que l'histoire, la civilisation et les valeurs de la liberté et de la démocratie ont tissé entre nos deux peuples.
>
> Je veux d'une France qui parle toujours à l'Amérique comme une amie, qui lui dit toujours la vérité et qui sait lui dire non quand elle a tort, qui lui dit qu'elle n'a pas raison quand elle viole le droit des nations ou le droit des gens qu'elle a tant contribué à forger, quand elle décide unilatéralement, quand elle veut américaniser le monde alors qu'elle a toujours défendu la liberté des peuples.
>
> Je veux lui dire que je crois à la pluralité des cultures et pas à la culture unique fût-elle américaine.
>
> Je veux être le Président d'une France qui s'adresse à l'Amérique comme un peuple libre à un autre peuple libre qui se comprennent et qui se respectent.
>
> Je veux être le Président d'une France qui ne transigera jamais sur son indépendance ni sur ses valeurs. Je veux rendre hommage à Jacques Chirac, qui a fait honneur à la France quand il s'est opposé à la guerre en Irak, qui était une faute.
>
> Je veux être le Président d'une France qui se donnera les moyens d'une défense à la hauteur du rôle éminent qu'elle veut continuer à jouer sur la scène du monde.
>
> Je veux être le Président de la France des droits de l'homme. Chaque fois qu'une femme est martyrisée dans le monde, la France doit se porter à ses côtés. La France, si les Français me choisissent comme Président, sera aux côtés des infirmières bulgares condamnées à mort en Libye. Elle sera aux côtés de la femme qui risque la lapidation parce qu'elle est soupçonnée d'adultère. Elle sera aux côtés de la persécutée qu'on oblige à porter la burka, aux côtés de la malheureuse qu'on oblige à prendre un mari qu'on lui a choisi, aux côtés de celle à laquelle son frère interdit de se mettre en jupe. Aux côtés de l'enfant que l'on vend ou que l'on exploite.
>
> Je ne crois pas à la " realpolitik " qui fait renoncer à ses valeurs sans gagner des contrats. Je n'accepte pas ce qui se passe en Tchétchénie, au Darfour. Je n'accepte pas le sort que l'on fait aux dissidents dans de nombreux pays. Je n'accepte pas la répression contre les journalistes que l'on veut bâillonner. Le silence est complice. Je ne veux être le complice d'aucune dictature à travers le monde.
>
> Je veux être le Président d'une France qui dira à tous les hommes  :  " Nous ne pouvons plus continuer de détruire notre planète. Nous ne pouvons plus continuer de sacrifier le bien être des générations futures aux excès des générations d'aujourd'hui. C'est l'avenir de l'Humanité qui est en jeu. C'est la paix du monde qui est en péril. Car, si nous continuons, le réchauffement climatique, l'épuisement des ressources, les pollutions déplaceront les peuples et les précipiteront dans des guerres qui seront les plus terribles de toutes les guerres parce que ce seront des guerres de l'eau et de la faim et qu'elles seront les plus désespérées.
>
> Nous avions cru entrer dans le monde de l'abondance. C'est le monde de la rareté que nous préparons à nos enfants, et la rareté engendre la violence.
>
> La mondialisation de l'économie, n'offrira une espérance nouvelle aux peuples déshérités que si le développement durable et le codéveloppement apparaissent désormais comme des impératifs à toue l'humanité.
>
> Je veux être le Président d'une France qui montrera l'exemple au monde d'un pays qui engage sa jeunesse dans l'aide au développement, investira dans les technologies propres et les énergies nouvelles, réduira ses gaspillages, préparera l'évènement d'une société de modération à la place d'une société d'excès.
>
> La mondialisation nous oblige à tout réinventer, à nous penser sans cesse par rapport aux autres et pas seulement par rapport à nous-mêmes.
>
> - Je veux être le Président d'une France réunie.
>
> L'unité de la France je veux la faire par l'action. Cette unité je veux qu'elle soit comme une renaissance.
>
> Après mai 68, Georges Pompidou avait dit  :  " le monde a besoin d'une nouvelle Renaissance ". La Renaissance, ce temps où pour la première fois les hommes ont eu le sentiment que tout était possible.
>
> Tout paraissait possible aux hommes de la Renaissance. Tout paraissait possible à ceux des Lumières, à ceux de la Révolution, à ceux des 30 Glorieuses.
>
> Alors que le monde change à un rythme où jamais il n'a changé, alors que partout d'immenses forces de création sont à l'oeuvre, que partout les hommes se battent pour inventer, pour créer, pour s'arracher à la misère, pour tenter de se construire un nouveau monde, nous ne pouvons être immobiles, nous ne pouvons répondre au monde qui nous invite à le rejoindre dans sa course effrénée au changement  :  " à quoi bon ? " Voici le pays qui a inventé l'idée de progrès, qui a crié un jour à la face du monde  :  " le bonheur est une idée neuve ", le pays qui le premier a dit à l'Homme  :  " tu as des droits imprescriptibles ", le pays qui a passé avec la liberté du monde un pacte multiséculaire, le pays qui si souvent a été à l'avant-garde de la civilisation, le voici qui aujourd'hui semble avoir perdu cette foi en lui-même, cette conviction que le destin l'avait créé pour accomplir de grandes choses et pour éclairer l'humanité. Un doute s'est installé qui a peu à peu grandi, peu à peu sapé cette confiance qui fait la force des grandes nations. Ce doute terrible c'est le mal qu'il nous faut guérir pour que dans l'art, dans la science, dans l'économie, partout la vie explose de nouveau, partout l'intelligence et le travail humains se remettent à féconder l'avenir.
>
> Je veux être le Président d'une France qui aura compris que la création demain sera dans le mélange, dans l'ouverture, dans la rencontre. Qu'elle sera dans le croisement des regards, la fécondation réciproque des cultures, des techniques et des savoirs, qu'elle jaillira de la rencontre de l'artiste, du savant, de l'ingénieur, de l'entrepreneur, au croisement de la communication, de l'économie, des sciences, de toutes les formes d'art et de pensée, de travail, d'innovation.
>
> Je veux être le président d'une France qui incarnera l'audace, l'intelligence et la création.
>
> Je veux être le président d'une France qui ne s'enfermera pas dans son histoire pour échapper à l'avenir, qui ne sera pas un musée, mais qui saura s'adosser à son histoire pour s'élancer vers le futur.
>
> Mes amis, la tâche est immense. Mais elle en vaut la peine.
>
> Je demande à ma famille de m'aider. Je sais ce qu'elle a eu à souffrir. Je veux qu'elle comprenne que ce n'est pas de moi qu'il s'agit mais de la France.
>
> Je demande à mes amis qui m'ont accompagné jusqu'ici de me laisser libre, libre d'aller vers les autres, vers celui qui n'a jamais été mon ami, qui n'a jamais appartenu à notre camp, à notre famille politique qui parfois nous a combattu. Parce que lorsqu'il s'agit de la France, il n'y a plus de camp.
>
> Je demande à vous tous de comprendre que je ne serai pas que le candidat de l'UMP, qu'au moment même où vous m'avez choisi je dois me tourner vers tous les Français, quels que soient leur parcours, qu'ils soient de droite ou de gauche, de métropole ou d'Outre Mer, qu'ils vivent en France ou à l'étranger, que la France les ait ou non déçu pourvu qu'il l'aiment. Que je dois les rassembler, que je dois les convaincre qu'ensemble tout deviendra possible ! Tout deviendra possible pour la France, Tout deviendra possible si vous le voulez, Tout deviendra possible si vous le décidez.
>
> Vive la République, Vive la France
>
""".lower().count("france")
)
