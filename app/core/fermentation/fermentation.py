import time


class Fermentation:

    def __init__(self, ph_val: float, lac_bac: float, str_bac: float):
        """
        initialize with the concentration of pH, lactobacillus and streptococcus
        prepare data for the fermentation process.
        """
        self.ph_val = ph_val
        self.lac_bac = lac_bac
        self.str_bac = str_bac
        self._init_process()

    def _init_process(self):
        # First process
        print("[*] In the first process the pH value decrease from {} to 6.0".format(self.ph_val))
        print("[*] Small amount of choloidal calcium phosphate\n\n")
        time.sleep(1)
        self.ph_val = 5.0
        print("[*] In the second process  the ph is decreased to {}".format(self.ph_val))
        time.sleep(1)
        print("[*] In the third process the ph decrease to 4.6, casein is added in gel matrix")


