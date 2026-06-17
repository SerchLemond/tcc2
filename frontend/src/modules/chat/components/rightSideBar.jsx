import { Button } from "@/components/ui/button";
import { ScrollArea } from "@/components/ui/scroll-area";
import { Separator } from "@/components/ui/separator";
import { BookOpen, Database, Download, Eye, FileBarChart, PieChart } from "lucide-react";
const RightSideBar = () => {
    return (<div className="w-64 bg-white border-l border-gray-100 mt-14">
            <ScrollArea className="h-full">
                <div className="p-4">
                    {/* Related Resources */}
                    <div className="mb-5">
                        <h3 className="text-xs font-medium text-gray-700 mb-2 uppercase tracking-wider">Recursos Relacionados</h3>
                        <div className="space-y-1">
                            <Button variant="ghost" size="sm" className="w-full justify-start text-gray-500 hover:text-gray-800 font-normal text-sm h-8">
                                <Database className="w-4 h-4 mr-3 text-gray-400"/>
                                Base de Dados OMS
                            </Button>
                            <Button variant="ghost" size="sm" className="w-full justify-start text-gray-500 hover:text-gray-800 font-normal text-sm h-8">
                                <BookOpen className="w-4 h-4 mr-3 text-gray-400"/>
                                Protocolos de Pesquisa
                            </Button>
                            <Button variant="ghost" size="sm" className="w-full justify-start text-gray-500 hover:text-gray-800 font-normal text-sm h-8">
                                <FileBarChart className="w-4 h-4 mr-3 text-gray-400"/>
                                Artigos Relacionados
                            </Button>
                        </div>
                    </div>

                    <Separator className="my-3"/>

                    {/* Analysis Tools */}
                    <div>
                        <h3 className="text-xs font-medium text-gray-700 mb-2 uppercase tracking-wider">
                            Ferramentas de Análise
                        </h3>
                        <div className="space-y-1">
                            <Button variant="ghost" size="sm" className="w-full justify-start text-gray-500 hover:text-gray-800 font-normal text-sm h-8">
                                <PieChart className="w-4 h-4 mr-3 text-gray-400"/>
                                Análise Estatística
                            </Button>
                            <Button variant="ghost" size="sm" className="w-full justify-start text-gray-500 hover:text-gray-800 font-normal text-sm h-8">
                                <Eye className="w-4 h-4 mr-3 text-gray-400"/>
                                Visualização de Dados
                            </Button>
                            <Button variant="ghost" size="sm" className="w-full justify-start text-gray-500 hover:text-gray-800 font-normal text-sm h-8">
                                <Download className="w-4 h-4 mr-3 text-gray-400"/>
                                Exportar Relatório
                            </Button>
                        </div>
                    </div>
                </div>
            </ScrollArea>
        </div>);
};
export default RightSideBar;
