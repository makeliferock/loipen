-- name = "Loipen Bericht"
-- description = "bergfex.com"
-- data_source = "bergfex.com"
-- type = "widget"
-- author = "stefan"
-- version = "1.0"

local json = require "json"

function on_alarm()
  http:get("https://makeliferock.github.io/loipen/loipen.json")
end

function on_network_result(result)
  local out = ""
  local t = json.decode(result)
  local tim = t.timestamp
  out = out..tim.."\n"
  local loips = t.loipen
  out = out..loips[1].loipe.." "..loips[1].status.."\n"
  out = out..loips[2].loipe.." "..loips[2].status --.."\n"
  --out = out..loips[3].loipe.." "..loips[3].status

  ui:show_text(out)
end

function on_click()

end
