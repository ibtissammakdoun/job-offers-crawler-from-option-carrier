# job-offers-crawler-from-option-carrier
This folder contains scripts to allow data scrawling from optioncarriere.ma website and save data on MongoDb

documents to be collected:

- **link**: *(character)* the link to the job offer
- **title**: *(character)* the title of the job offer
- **details**: *(list)* a list that can contains the city, the contract and/or the salary
- **company**: *(character)* the company name (not always listed)
- **tags**: *(list)* contains the date of publication of the offer
- **description**: *(dictionnary)*
    this fiels is another document that cintainds the content of the job mission, profile and poste data
      - **desc** : *(text)* the content of the job offer
      - **mission**: *(list)* only missions on the job offer
      - **profile** : *(list)* candidate profil
      - **post**: *(list)* information about the posting
      - **phrases**: *(list)* phrases extracted from the job offer
- **insert_time**: *(date)* the date of insert

