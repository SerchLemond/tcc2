import { Button } from "@/components/ui/button";
import { ScrollArea } from "@/components/ui/scroll-area";
const LeftSideBar = () => {
    return (<div className="fixed top-14 bottom-0 w-64 bg-white border-r border-gray-100 hidden md:block">
            <ScrollArea className="h-full">
                <div className="p-4">
                    <div className="mb-5">
                        <h3 className="text-xs font-medium text-gray-700 mb-2 uppercase tracking-wider">Chats</h3>
                        <div className="space-y-1">
                            <Button variant="ghost" size="sm" className="w-full justify-start text-gray-500 hover:text-gray-200 font-normal text-sm h-8">
                                Chat 1
                            </Button>
                        </div>
                    </div>
                </div>
            </ScrollArea>
        </div>);
};
export default LeftSideBar;
