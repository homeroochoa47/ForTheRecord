import { extendTheme } from "@chakra-ui/react";
import { mode } from "@chakra-ui/theme-tools";

const theme = extendTheme({
  config,
  styles: {
    global: (props) => ({
      body: {
        bg: mode("#698396", "#6cabd4")(props),
      }
    })
  },
})