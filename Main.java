import java.io.PrintStream;
import java.nio.charset.StandardCharsets;
import java.nio.file.Path;
import java.util.HashMap;
import java.util.List;

public class Main {
    
    public static void main(String[] args) {
        
        System.setOut(new PrintStream(
            System.out, true, StandardCharsets.UTF_8
        ));
        
        Builder build = new Builder();

        HashMap<List<String>, HashMap<String, Integer>> map = build.build(Path.of("story1.txt"), 2);

        build.read(map, 100);

    }

}
