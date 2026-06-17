
import {
  Settings,
} from "lucide-react"

const Header = () => {
    return (
        <div className="fixed top-0 left-0 right-0 z-10 bg-white border-b border-gray-100">
            <div className="flex items-center justify-between px-5 py-2">
                <div className="flex items-center space-x-3">
                    <div className="w-7 h-7 bg-blue-600 rounded-lg flex items-center justify-center">
                        <Settings className="w-4 h-4 text-white" />
                    </div>
                    <div>
                        <h1 className="text-base font-semibold text-gray-800">Epi Research</h1>
                        <p className="text-xs text-gray-500">Sistema de Pesquisa Epidemiológica</p>
                    </div>
                </div>
                {/* <nav className="flex items-center space-x-6">
                    <Button variant="ghost" size="sm" className="text-gray-500 font-normal">
                        <Settings className="w-4 h-4 mr-2" />
                        Painel
                    </Button>
                    <Button variant="ghost" size="sm" className="text-gray-500 font-normal">
                        <Search className="w-4 h-4 mr-2" />
                        Pesquisas
                    </Button>
                    <Button variant="ghost" size="sm" className="text-gray-500 font-normal">
                        <FileText className="w-4 h-4 mr-2" />
                        Documentação
                    </Button>
                    <Button variant="ghost" size="sm" className="text-gray-500 font-normal">
                        <HelpCircle className="w-4 h-4 mr-2" />
                        Suporte
                    </Button>
                </nav> */}
            </div>
        </div>
    )
}

export default Header