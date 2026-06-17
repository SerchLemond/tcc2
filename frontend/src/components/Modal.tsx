import * as Plot from "@observablehq/plot";
import PlotFigure from "./ui/PlotFigure";
import { useState, useEffect } from "react";
import { Button } from "@/components/ui/button"

interface ModalProps {
  isOpen: boolean
  setIsOpen: React.Dispatch<React.SetStateAction<boolean>>
  json_plot?: JsonVisualizacoes
}

interface Visualizacao {
  tipo: string;
  score: number;
  titulo: string;
  pergunta: string;
  dados: Dado[];
}

interface Dado {
  dimensoes: Record<string, string | number>; // chave-valor genérico para qualquer dimensão
  valor: number;
}

interface JsonVisualizacoes {
  visualizacoes: Visualizacao[];
}

const plotsLocalStorage = (vis: Visualizacao) => {
  let plots = localStorage.getItem("plots")
  let plotsList:Visualizacao[] = []
  if(plots === null) {
    plotsList.push(vis)
  } else {
    plotsList = JSON.parse(plots)
    plotsList.push(vis)
  }
  localStorage.setItem("plots", JSON.stringify(plotsList));
}

function temValores(vis: any, dim: any) {
  if (!dim) return false; // não existe
  return vis.dados.some((d:any) => d.dimensoes[dim] !== undefined && d.dimensoes[dim] !== null);
}

export default function Modal({ isOpen, setIsOpen, json_plot }: ModalProps) {
  if (!isOpen) return null
  if (!json_plot) {
    console.log("não tem nada no json")
    return null
  }

  const [brasil, setBrasil] = useState({})
  const [selectedIndex, setSelectedIndex] = useState<number | null>(null);
  useEffect(() => {
    fetch("https://raw.githubusercontent.com/giuliano-macedo/geodata-br-states/refs/heads/main/geojson/br_states.json", {
      method: "GET"
    })
      .then((res) => res.json())
      .then((data) => setBrasil(data))
      .catch((error) => console.log(error))
  }, [])

   const renderPlot = (vis: any) => {
    switch (vis.tipo) {
      case "grafico_barras_horizontal": {
        const dimensao = Object.keys(vis.dados[0].dimensoes)[0]; // pega a chave da dimensão
        const dadosFormatados = vis.dados.map((d: Dado) => ({ ...d.dimensoes, valor: d.valor }));

        return (
          <PlotFigure
            options={{
              width: 600,
              height: 600,
              marks: [
                Plot.barX(dadosFormatados, { x: "valor", y: dimensao, fill: "steelblue" })
              ],
              x: { grid: true, axis: "both" },
              marginLeft: 120
            }}
          />
        );}
      case "grafico_barras_vertical": {
        const dimensao = Object.keys(vis.dados[0].dimensoes)[0]; // pega a chave da dimensão
        const dadosFormatados = vis.dados.map((d: Dado) => ({ ...d.dimensoes, valor: d.valor }));

        return (
          <PlotFigure
            options={{
              width: 600,
              height: 600,
              marks: [
                Plot.barY(dadosFormatados, { x: dimensao, y: "valor", fill: "steelblue" })
              ],
              x: { tickRotate: -45 }, // gira os rótulos
              marginBottom: 100
            }}
          />
      );}
      case "graficos_linhas": {
        const dims = vis.dados[0].dimensoes;

        // Detecta automaticamente as chaves de dimensão
        const chaveNumerica = Object.keys(dims).find(k => typeof dims[k] === "number"); // Ex: "id_ano"
        const chaveTexto = Object.keys(dims).find(k => typeof dims[k] === "string"); // Ex: "Ano de Notificação"

        if (!chaveNumerica || !chaveTexto) return null; // Proteção

        // 1. Ordena os dados pelo ID numérico (ex: 2020, 2021, 2022...)
        const dadosOrdenados = [...vis.dados].sort(
            (a, b) => (a.dimensoes[chaveNumerica] as number) - (b.dimensoes[chaveNumerica] as number)
        ); 

        // 2. Extrai apenas os valores formatados para o Plot
        const dadosFormatados = dadosOrdenados.map((d: Dado) => ({
            // Usar a chave de texto para o eixo X
            [chaveTexto]: d.dimensoes[chaveTexto], 
            valor: d.valor
        }));
        
        // 3. Define a ordem do domínio para garantir que o eixo X siga a ordem do ano.
        const domainOrder = dadosOrdenados.map(d => d.dimensoes[chaveTexto] as string);

        // console.log(dadosFormatados);
        // console.log(domainOrder); // Deve ser a lista de rótulos na ordem correta

        return (
            <PlotFigure
                options={{
                    width: 600,
                    height: 600,
                    marks: [
                        Plot.line(dadosFormatados, { 
                            // Agora 'x' usa a chave de texto (rótulo)
                            x: chaveTexto, 
                            y: "valor", 
                            stroke: "steelblue"
                        }),
                        Plot.dot(dadosFormatados, { 
                            x: chaveTexto, 
                            y: "valor", 
                            fill: "darkblue"
                        }),
                    ],
                    x: { 
                        domain: domainOrder, // Garante a ordem correta dos rótulos
                        label: chaveTexto,
                        tickRotate: -45,
                        padding: 0.1 // Adiciona um pequeno espaço nas bordas
                    },
                    y: { 
                        grid: true,
                        label: "Valor"
                    },
                    marginBottom: 100 // Aumenta para acomodar os rótulos girados
                }}
            />
        );
      }

      case "mapas_coropleticos":
         return (
          <PlotFigure
            options={{
              width: 600,
              height: 600,
              axis: null,
              color: {
                type: "quantize",
                scheme: "blues",
                label: "Valor",
                legend: true
              },
              marks: [
                Plot.geo(brasil, { 
                  fill: (elemento: any) => {
                    const estado = elemento.properties.Estado;
                    return vis.dados.find((d: Dado) => Object.values(d.dimensoes)[0] === estado)?.valor;
                  },
                  stroke: "lightgray"
                })
              ]
            }}
          />
        );
      case "graficos_com_proporcao":
        const primeiraDim = Object.keys(vis.dados[0].dimensoes)[0];
        const segundaDim = Object.keys(vis.dados[0].dimensoes)[1];
        const terceiraDim = Object.keys(vis.dados[0].dimensoes)[2];

        const fillDim =
          temValores(vis, terceiraDim) ? terceiraDim :
          temValores(vis, segundaDim)  ? segundaDim  :
          primeiraDim;

        return (
        <PlotFigure
          options={{
            width: 600,
            height: 600,
            x: { label: primeiraDim, tickRotate: -40 },
            y: { label: "Valor" },
            color: { legend: true },
            marks: [
              Plot.barY(vis.dados.map((d: Dado) => ({ ...d.dimensoes, valor: d.valor })), {
                x: primeiraDim,
                y: "valor",
                fill: fillDim
              })
            ],
            marginBottom: 120,
          }}
        />
      );
      default:
        return null
  }}

  return (
    <>
      {/* Fundo escuro semi-transparente */}
      <div
        className="fixed inset-0 bg-black/50 z-40"
        onClick={() => setIsOpen(false)} // fecha ao clicar no fundo
      />

       <div className="fixed top-1/2 left-1/2 w-fit max-h-screen -translate-x-1/2 -translate-y-1/2 bg-white z-50 rounded-lg shadow-lg px-4 py-8 flex flex-row gap-6 overflow-y-auto justify-center items-center">
        {json_plot?.visualizacoes
          .filter((vis) => vis.score >= 0.8)
          .map((vis, index) => {
            // impede a renderização dos gráficos nao selecionados
            if (selectedIndex !== null && selectedIndex !== index) return null;
            
            // retorna o gráfico selecionado ou os outros graficos
            return (
              <div className="flex flex-col">
                <p 
                  className={"text-center font-semibold" + 
                  ((selectedIndex !== null && selectedIndex !== index)
                    ? "my-4 text-[12px]"
                    : "mt-2 mb-6 text-base")}>
                  {vis.titulo}
                </p>
                <div
                  key={index}
                  className={`cursor-pointer transition-all` + (selectedIndex === null ? `w-fit` : `max-w-[250px]`)}
                  onClick={() =>
                    setSelectedIndex(selectedIndex === index ? null : index)
                  }
                >
                  {renderPlot(vis)}
                  {selectedIndex !== null && (
                    <div className="text-center w-full mt-6">
                      <Button 
                        size="sm" 
                        className="bg-blue-600 hover:bg-blue-700" 
                        onClick={(e)=> {
                          e.stopPropagation(); 
                          plotsLocalStorage(vis);
                        }}>
                          Armazenar gráfico
                        </Button>
                    </div>

                  )}
                </div>
              </div>
            );
          })}
      </div>
    </>
  )
}
