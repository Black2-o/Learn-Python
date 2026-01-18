import { Avatar, AvatarFallback, AvatarImage } from "@/components/ui/avatar"
import { Link } from "react-router-dom"
import { Moon, Sun } from "lucide-react"
import { Button } from "@/components/ui/button"
import {
    DropdownMenu,
    DropdownMenuContent,
    DropdownMenuItem,
    DropdownMenuTrigger,
} from "@/components/ui/dropdown-menu"
import { useTheme } from "@/components/ThemeProvider"


export function Navbar() {
    const { setTheme } = useTheme()

    return (
        <nav className="fixed top-0 left-0 w-full flex items-center justify-between px-4 md:px-6 py-3 border-b shadow-sm z-999 bg-white dark:bg-gray-900 border-b-slate-200 dark:border-b-slate-700 h-16">
            {/* Left Section: Logo & Mobile Menu */}
            <div className="flex items-center gap-4">
                {/* Logo */}
                <div className="flex items-center">
                    <Link to="/dashboard" className="hover:opacity-80 transition-opacity duration-200">
                        <h1 className="text-xl font-bold">FastAPI Microservices</h1>
                    </Link>
                </div>
            </div>


            {/* Right Section: Notifications & User Menu */}
            <div className="flex items-center gap-4">
                <DropdownMenu>
                    <DropdownMenuTrigger asChild>
                        <Button variant="outline" size="icon">
                            <Sun className="h-[1.2rem] w-[1.2rem] scale-100 rotate-0 transition-all dark:scale-0 dark:-rotate-90" />
                            <Moon className="absolute h-[1.2rem] w-[1.2rem] scale-0 rotate-90 transition-all dark:scale-100 dark:rotate-0" />
                            <span className="sr-only">Toggle theme</span>
                        </Button>
                    </DropdownMenuTrigger>
                    <DropdownMenuContent align="end">
                        <DropdownMenuItem onClick={() => setTheme("light")}>
                            Light
                        </DropdownMenuItem>
                        <DropdownMenuItem onClick={() => setTheme("dark")}>
                            Dark
                        </DropdownMenuItem>
                        <DropdownMenuItem onClick={() => setTheme("system")}>
                            System
                        </DropdownMenuItem>
                    </DropdownMenuContent>
                </DropdownMenu>
                <Avatar>
                    <AvatarImage src="https://i.pravatar.cc/150" />
                    <AvatarFallback>B2</AvatarFallback>
                </Avatar>
            </div>



        </nav>
    )
}

export default Navbar