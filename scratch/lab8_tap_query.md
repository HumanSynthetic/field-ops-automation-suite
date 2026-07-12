# Temporary Lab 8 catalogue query

[Run the Pleiades Section B Hipparcos query](https://tapvizier.cds.unistra.fr/TAPVizieR/tap/sync?request=doQuery&lang=ADQL&format=csv&query=SELECT+TOP+100+HIP%2C+%22_RA.icrs%22+AS+RAdeg%2C+%22_DE.icrs%22+AS+DEdeg%2C+Vmag%2C+%22B-V%22+AS+BV%0AFROM+%22I%2F239%2Fhip_main%22%0AWHERE+1%3DCONTAINS%28POINT%28%27ICRS%27%2C+%22_RA.icrs%22%2C+%22_DE.icrs%22%29%2C+POLYGON%28%27ICRS%27%2C+57.5764%2C+24.2902%2C+57.2354%2C+24.7277%2C+56.5968%2C+24.3203%2C+56.9377%2C+23.883%29%29%0AAND+Vmag+IS+NOT+NULL+AND+%22B-V%22+IS+NOT+NULL%0AORDER+BY+Vmag)
