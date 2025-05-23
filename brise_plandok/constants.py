ATTRIBUTE_NORM_MAP = {
    "Verkehrsflaeche_ID": "VerkehrsflaecheID",
    "VorkehrungBepflanzungOeffentlicheVerkehrsflaeche": "VorkehrungBepflanzung",
    "AnBaulinie": "AnFluchtlinie",
    "AnStrassenfluchtlinie": "AnFluchtlinie",
    "Bauklasse_ID": "Bauklasse",
    "HochhausUnzulaessigGemaessBB": "HochhausZulaessigGemaessBB",
    "StruktureinheitBebaubar": "Struktureinheit",
}

GOLD_PREFIX = "GOLD"
GOLD_COLOR = "FFD700"
GRAY_COLOR = "DCDCDC"

ROW_HEIGHT = 75

ANNOTATOR_NAME_INDEX = -4
DO_NOT_ANNOTATE = "DON'T ANNOTATE THIS SENTENCE"

DATA_FOLDER = "data"
TRAIN = "train"
VALID = "valid"
TEST = "test"


class Review:
    OK = "OK"
    MISSING = "MISSING"
    ERROR = "ERROR"


class DocumentFields:
    ID = "id"
    SENS = "sens"
    ANNOTATORS = "annotators"
    FULL_ANNOTATORS = "full_annotators"
    LABELS_GOLD = "labels_gold"
    FULL_GOLD = "full_gold"
    LABELS_REVIEWERS = "labels_reviewers"
    FULL_REVIEWERS = "full_reviewers"


class SenFields:
    ID = "id"
    TEXT = "text"
    GOLD_MODALITY = "gold_modality"
    ALREADY_GOLD_ON_ANNOTATION = "already_gold_on_annotation"
    GEN_ATTRIBUTES_ON_ANNOTATION = "gen_attributes_on_annotation"
    GEN_ATTRIBUTES_ON_FULL_ANNOTATION = "gen_attributes_on_full_annotation"
    GEN_ATTRIBUTES = "gen_attributes"
    LABELS_GOLD_EXISTS = "labels_gold_exists"
    FULL_GOLD_EXISTS = "full_gold_exists"
    GOLD_ATTRIBUTES = "gold_attributes"
    ANNOTATED_ATTRIBUTES = "annotated_attributes"
    FULL_ANNOTATED_ATTRIBUTES = "full_annotated_attributes"
    ATTRIBUTES = "attributes"
    SEGMENTATION_ERROR = "segmentation_error"
    PREDICTED_ATTRIBUTES = "predicted_attributes"
    PREDICTED_MODALITY = "predicted_modality"


class AttributeFields:
    NAME = "name"
    TYPE = "type"
    VALUE = "value"


class AnnotatedAttributeFields:
    ANNOTATORS = "annotators"


class FullAnnotatedAttributeFields:
    ATTRIBUTES = "attributes"
    MODALITY = "modality"


class OldDocumentFields:
    ID = "id"
    SECTIONS = "sections"


class OldSectionFields:
    SENS = "sens"


class OldSenFields:
    ID = "sen_id"
    TEXT = "text"
    GEN_ATTRIBUTES = "gen_attributes"
    ATTRIBUTES = "attributes"


class AttributesNames:
    AbschlussDachMaxBezugGebaeude = "AbschlussDachMaxBezugGebaeude"
    AbschlussDachMaxBezugGelaende = "AbschlussDachMaxBezugGelaende"
    AnFluchtlinie = "AnFluchtlinie"
    AnlageZumEinstellenVorhanden = "AnlageZumEinstellenVorhanden"
    AnOeffentlichenVerkehrsflaechen = "AnOeffentlichenVerkehrsflaechen"
    AnordnungGaertnerischeAusgestaltung = "AnordnungGaertnerischeAusgestaltung"
    AnordnungGaertnerischeAusgestaltungProzentual = "AnordnungGaertnerischeAusgestaltungProzentual"
    AnteilBaumbepflanzung = "AnteilBaumbepflanzung"
    AnteilDachbegruenung = "AnteilDachbegruenung"
    AnzahlGebaeudeMax = "AnzahlGebaeudeMax"
    ArkadeHoehe = "ArkadeHoehe"
    AufbautenZulaessig = "AufbautenZulaessig"
    AusnahmeGaertnerischAuszugestaltende = "AusnahmeGaertnerischAuszugestaltende"
    AusnahmeVonWohnungenUnzulaessig = "AusnahmeVonWohnungenUnzulaessig"
    Bauklasse = "Bauklasse"
    BauweiseID = "BauweiseID"
    BebauteFlaecheMax = "BebauteFlaecheMax"
    BebauteFlaecheMaxNebengebaeude = "BebauteFlaecheMaxNebengebaeude"
    BebauteFlaecheMaxProzentual = "BebauteFlaecheMaxProzentual"
    BebauteFlaecheMin = "BebauteFlaecheMin"
    BegruenungDach = "BegruenungDach"
    Dachart = "Dachart"
    DachflaecheMin = "DachflaecheMin"
    DachneigungMax = "DachneigungMax"
    DachneigungMin = "DachneigungMin"
    DurchfahrtBreite = "DurchfahrtBreite"
    DurchfahrtHoehe = "DurchfahrtHoehe"
    DurchgangBreite = "DurchgangBreite"
    DurchgangHoehe = "DurchgangHoehe"
    EinfriedungAusgestaltung = "EinfriedungAusgestaltung"
    EinfriedungHoeheGesamt = "EinfriedungHoeheGesamt"
    EinfriedungLage = "EinfriedungLage"
    EinfriedungZulaessig = "EinfriedungZulaessig"
    EinleitungNiederschlagswaesser = "EinleitungNiederschlagswaesser"
    ErrichtungGebaeude = "ErrichtungGebaeude"
    FBOKMinimumWohnungen = "FBOKMinimumWohnungen"
    GebaeudeBautyp = "GebaeudeBautyp"
    GebaeudeHoeheArt = "GebaeudeHoeheArt"
    GebaeudeHoeheMaxAbsolut = "GebaeudeHoeheMaxAbsolut"
    GebaeudeHoeheMaxWN = "GebaeudeHoeheMaxWN"
    GebaeudeHoeheMin = "GebaeudeHoeheMin"
    GehsteigbreiteMin = "GehsteigbreiteMin"
    GaragengebaeudeAusfuehrung = "GaragengebaeudeAusfuehrung"
    GesamtePlangebiet = "GesamtePlangebiet"
    HoehenlageGrundflaeche = "HoehenlageGrundflaeche"
    InSchutzzone = "InSchutzzone"
    Kleinhaeuser = "Kleinhaeuser"
    MaxAnzahlGeschosseOberirdisch = "MaxAnzahlGeschosseOberirdisch"
    MindestraumhoeheEG = "MindestraumhoeheEG"
    OeffentlicheVerkehrsflaecheBreiteMin = "OeffentlicheVerkehrsflaecheBreiteMin"
    Planzeichen = "Planzeichen"
    StellplatzImNiveauZulaessig = "StellplatzImNiveauZulaessig"
    StellplatzregulativUmfangMaximumAbsolut = "StellplatzregulativUmfangMaximumAbsolut"
    StellplatzregulativUmfangMaximumRelativ = "StellplatzregulativUmfangMaximumRelativ"
    StellplatzregulativUmfangMinimumRelativ = "StellplatzregulativUmfangMinimumRelativ"
    Stockwerk = "Stockwerk"
    StrassenbreiteMax = "StrassenbreiteMax"
    StrassenbreiteMin = "StrassenbreiteMin"
    StrassenbreiteVonBis = "StrassenbreiteVonBis"
    Struktureinheit = "Struktureinheit"
    TechnischeAufbautenHoeheMax = "TechnischeAufbautenHoeheMax"
    UnterbrechungGeschlosseneBauweise = "UnterbrechungGeschlosseneBauweise"
    UnterirdischeBaulichkeiten = "UnterirdischeBaulichkeiten"
    VerbotBueroGeschaeftsgebaeude = "VerbotBueroGeschaeftsgebaeude"
    VerbotFensterZuOeffentlichenVerkehrsflaechen = "VerbotFensterZuOeffentlichenVerkehrsflaechen"
    VerbotStaffelung = "VerbotStaffelung"
    VerbotWohnung = "VerbotWohnung"
    VerkehrsflaecheID = "VerkehrsflaecheID"
    VolumenUndUmbaubarerRaum = "VolumenUndUmbaubarerRaum"
    VorbautenBeschraenkung = "VorbautenBeschraenkung"
    VorbautenVerbot = "VorbautenVerbot"
    VonBebauungFreizuhalten = "VonBebauungFreizuhalten"
    VorkehrungBepflanzung = "VorkehrungBepflanzung"
    VorstehendeBauelementeAusladungMax = "VorstehendeBauelementeAusladungMax"
    WidmungInMehrerenEbenen = "WidmungInMehrerenEbenen"
    Widmung = "Widmung"
    Nutzungsart = "Nutzungsart"
    BBAllgemein = "BBAllgemein"


class AttributeTypes:
    CONDITION = "condition"
    CONTENT = "content"
    CONDITION_EXCEPTION = "conditionException"
    CONTENT_EXCEPTION = "contentException"


class Modalities:
    OBLIGATION = "obligation"
    PERMISSION = "permission"
    PROHIBITION = "prohibition"


class SenToAttrFields:
    ATTR = "attr"
    SENS = "sens"
    MOD = "mod"


EMPTY = "EMPTY"
