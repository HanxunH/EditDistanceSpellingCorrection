import utilHelper as helper
import autocorrect

class coconutOrcas:
    def main(self):
        autocorrectTest = autocorrect.autoCorrectMethods()
        print autocorrectTest.globalEditDistence("crat","arts")
        print autocorrectTest.localEditDistence("cart","arts")
        print autocorrectTest.nGram("crat","cart",2)
        print autocorrectTest.nGram("crat","arts",2)
        return


runable = coconutOrcas()
runable.main()
