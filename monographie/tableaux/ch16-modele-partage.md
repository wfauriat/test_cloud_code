| Grandeur | Contrôle entre pairs | Un modèle pour tous | Modèle partagé, contrôleur précis | Indépendant et précis |
|:------------------------------------------------|----------:|---------:|----------------:|------------:|
| Taux d’erreur du producteur P(faux) | 10 % | 2 % | 2 % | 2 % |
| Causes d’erreur partagées c | 10 % | 60 % | 60 % | 10 % |
| Oubli sur les autres erreurs m | 20 % | 20 % | 20 % | 10 % |
| Taux de fausses alertes f | 5 % | 5 % | 0,5 % | 0,5 % |
| Sensibilité (1 − c)(1 − m) | 72 % | 32 % | 32 % | 81 % |
| Alertes qui sont de vraies erreurs (VPP) | 61,5 % | 11,6 % | 56,6 % | 76,8 % |
| Alertes par vraie erreur attrapée (1/VPP) | 1,6 | 8,7 | 1,8 | 1,3 |
| Échappement, alertes suivies à hauteur de la VPP | 55,7 % | 96,3 % | 81,9 % | 37,8 % |
| Échappement, chaque alerte examinée | 28,0 % | 68,0 % | 68,0 % | 19,0 % |
| Risque, alertes suivies à hauteur de la VPP | 5,57 % | 1,93 % | 1,64 % | 0,756 % |
| Risque, chaque alerte examinée | 2,80 % | 1,36 % | 1,36 % | 0,380 % |
| Risque sans contrôleur | 10 % | 2 % | 2 % | 2 % |

Table: Quand producteur et contrôleur partagent un même modèle : corrélation et fausses alertes. {#tbl:ch16-modele-partage}
