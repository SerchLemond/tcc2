"use client";
import { useEffect, useState } from "react";
import { Button } from "@/components/ui/button";
import Header from "./components/header";
import { useNavigate } from "react-router-dom";
import PlotGeneric from "@/components/ui/plot";
import { IoIosInformationCircleOutline } from "react-icons/io";
import { Dialog, DialogContent, DialogDescription, DialogHeader, DialogTitle, } from "@/components/ui/dialog";
import ChartInformation from "./components/chartInformation";
export default function DashboardPage() {
    const [plotList, setPlotList] = useState([]);
    const [openPlotIndex, setOpenPlotIndex] = useState(null);
    const [indexPlotModal, setIndexPlotModal] = useState(null);
    const navigate = useNavigate();
    useEffect(() => {
        const plots = localStorage.getItem("plots");
        if (plots !== null) {
            setPlotList(JSON.parse(plots));
        }
    }, []);
    return (<div className="flex h-screen bg-gray-50/50 overflow-hidden">
            <Header />

            <div className="flex-1 flex flex-col mt-14 overflow-hidden">
                {/* Header da conversa */}
                <div className="bg-white border-b border-gray-100 p-5 py-2 shrink-0 flex items-center justify-between">
                    <div>
                        <h2 className="text-lg font-medium text-gray-800">Dashboard de Pesquisa Epidemiológica</h2>
                        <p className="text-sm text-gray-500">Especializado em Tuberculose</p>
                    </div>
                    <div className="flex flex-row gap-4">
                        <Button size="sm" className="bg-blue-600 hover:bg-blue-700 text-white" onClick={() => navigate('/')}>
                            Voltar ao chat
                        </Button>
                    </div>
                </div>
                <div className="overflow-y-auto">
                    <div className="flex mx-5 my-3 gap-10 flex-wrap">
                        {plotList.map((plot, index) => (<div key={index} className="flex gap-4">
                                <div className="bg-white p-2 rounded-xl shadow-[0_4px_10px_rgba(0,0,0,0.07)] w-[530px] cursor-pointer" onClick={() => setIndexPlotModal(index)}>
                                    <p className="font-semibold text-center mt-2 mb-6 text-xl">{plot.titulo}</p>
                                    <PlotGeneric dados={plot.dados} tipo={plot.tipo}/>
                                </div>

                                <div className="cursor-pointer" onClick={() => setOpenPlotIndex(index)}>
                                    <IoIosInformationCircleOutline size={32}/>
                                </div>

                                <Dialog open={openPlotIndex === index} onOpenChange={(open) => setOpenPlotIndex(open ? index : null)}>
                                    <DialogContent className="max-w-4xl max-h-[90vh] overflow-y-auto">
                                        <DialogHeader>
                                            <DialogTitle>Informações do gráfico</DialogTitle>
                                            <DialogDescription>
                                                Estas são as informações que foram necessárias para a criação desse gráfico:
                                            </DialogDescription>
                                        </DialogHeader>

                                        <ChartInformation dados={JSON.stringify(plot.dados, null, 2)} pergunta={plot.pergunta} tipo={plot.tipo}/>

                                    </DialogContent>
                                </Dialog>
                            </div>))}
                    </div>
                </div>
            </div>
            <Dialog open={indexPlotModal !== null} onOpenChange={(open) => {
            if (!open)
                setIndexPlotModal(null); // fecha
        }}>
                <DialogContent className="max-w-4xl overflow-y-auto flex flex-col justify-center items-center">
                    {indexPlotModal !== null && (<>
                            <p className="font-semibold text-center mt-2 mb-6 text-xl">{plotList[indexPlotModal].titulo}</p>
                            <PlotGeneric dados={plotList[indexPlotModal].dados} tipo={plotList[indexPlotModal].tipo} tamanho={700}/>
                        </>)}
                </DialogContent>
            </Dialog>
        </div>);
}
