import java.nio.file.Path;
import java.util.HashMap;
import java.util.List;

public class Main {
    
    public static void main(String[] args) {
        
        Builder build = new Builder();

        HashMap<List<String>, HashMap<String, Integer>> map = build.build(Path.of("story1.txt"), 2);

        System.out.println(map);

    }

}
